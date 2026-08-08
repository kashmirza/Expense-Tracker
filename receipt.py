import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

from file_handler import load_data, save_data


# ==========================================================
# FILE SETTINGS
# ==========================================================

RECEIPT_FILE = "receipts.json"
RECEIPT_FOLDER = "receipts"

ALLOWED_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".pdf"
]


# ==========================================================
# CREATE RECEIPT FOLDER
# ==========================================================

if not os.path.exists(RECEIPT_FOLDER):
    os.makedirs(RECEIPT_FOLDER)


# ==========================================================
# RECEIPT MENU
# ==========================================================

def receipt_menu():

    while True:

        print("\n" + "=" * 60)
        print("                  🧾 RECEIPT MANAGEMENT")
        print("=" * 60)

        print("1. Upload Receipt")
        print("2. View My Receipts")
        print("3. Search Receipt")
        print("4. Delete Receipt")
        print("5. Back")

        print("=" * 60)

        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            return choice

        print("\n❌ Invalid Choice!")


# ==========================================================
# GENERATE RECEIPT ID
# ==========================================================

def generate_receipt_id(receipts):

    if not receipts:
        return "REC001"

    numbers = []

    for receipt in receipts:

        receipt_id = receipt.get("id", "")

        if receipt_id.startswith("REC"):

            try:
                number = int(receipt_id[3:])
                numbers.append(number)

            except ValueError:
                pass

    if not numbers:
        return "REC001"

    next_number = max(numbers) + 1

    return f"REC{next_number:03d}"


# ==========================================================
# UPLOAD RECEIPT
# ==========================================================

def upload_receipt(username):

    receipts = load_data(RECEIPT_FILE)

    if not isinstance(receipts, list):
        receipts = []

    print("\n" + "=" * 60)
    print("                  📤 UPLOAD RECEIPT")
    print("=" * 60)

    print("\nSupported files:")
    print("JPG, JPEG, PNG, PDF")

    # ------------------------------------------------------
    # Open File Selection Window
    # ------------------------------------------------------

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select Receipt",
        filetypes=[
            ("Receipt Files", "*.jpg *.jpeg *.png *.pdf"),
            ("JPG Files", "*.jpg"),
            ("JPEG Files", "*.jpeg"),
            ("PNG Files", "*.png"),
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        ]
    )

    root.destroy()

    # ------------------------------------------------------
    # Check Selection
    # ------------------------------------------------------

    if not file_path:

        print("\n❌ No file selected.")
        return

    # ------------------------------------------------------
    # Check File Exists
    # ------------------------------------------------------

    if not os.path.isfile(file_path):

        print("\n❌ File not found.")
        return

    # ------------------------------------------------------
    # Check Extension
    # ------------------------------------------------------

    extension = os.path.splitext(file_path)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        print("\n❌ Unsupported file type.")
        print("Allowed types: JPG, JPEG, PNG, PDF")
        return

    # ------------------------------------------------------
    # Receipt Title
    # ------------------------------------------------------

    title = input("Enter Receipt Title: ").strip()

    if not title:
        title = "Receipt"

    # ------------------------------------------------------
    # Description
    # ------------------------------------------------------

    description = input("Enter Description: ").strip()

    # ------------------------------------------------------
    # Generate Receipt ID
    # ------------------------------------------------------

    receipt_id = generate_receipt_id(receipts)

    # ------------------------------------------------------
    # Create Unique Filename
    # ------------------------------------------------------

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    original_name = os.path.basename(file_path)

    new_filename = (
        f"{receipt_id}_{timestamp}_{original_name}"
    )

    destination = os.path.join(
        RECEIPT_FOLDER,
        new_filename
    )

    # ------------------------------------------------------
    # Copy Receipt
    # ------------------------------------------------------

    try:

        shutil.copy2(file_path, destination)

    except Exception as error:

        print("\n❌ Could not upload receipt.")
        print(f"Error: {error}")
        return

    # ------------------------------------------------------
    # Save Receipt Information
    # ------------------------------------------------------

    now = datetime.now()

    receipt = {

        "id": receipt_id,

        "username": username,

        "title": title,

        "filename": new_filename,

        "path": destination,

        "description": description,

        "date": now.strftime("%Y-%m-%d"),

        "time": now.strftime("%I:%M %p")
    }

    receipts.append(receipt)

    save_data(RECEIPT_FILE, receipts)

    # ------------------------------------------------------
    # Success Message
    # ------------------------------------------------------

    print("\n" + "=" * 60)
    print("             ✅ RECEIPT UPLOADED")
    print("=" * 60)

    print(f"Receipt ID : {receipt['id']}")
    print(f"Title      : {receipt['title']}")
    print(f"File       : {receipt['filename']}")
    print(f"Date       : {receipt['date']}")
    print(f"Time       : {receipt['time']}")

    print("=" * 60)


# ==========================================================
# VIEW RECEIPTS
# ==========================================================

def view_receipts(username):

    receipts = load_data(RECEIPT_FILE)

    if not receipts:

        print("\n❌ No receipts found.")
        return

    user_receipts = [
        receipt
        for receipt in receipts
        if receipt.get("username") == username
    ]

    if not user_receipts:

        print("\n❌ You have not uploaded any receipts.")
        return

    print("\n" + "=" * 100)
    print("                         🧾 MY RECEIPTS")
    print("=" * 100)

    print(
        f"{'No':<5}"
        f"{'ID':<10}"
        f"{'Title':<20}"
        f"{'File':<35}"
        f"{'Date':<15}"
    )

    print("-" * 100)

    for index, receipt in enumerate(user_receipts, start=1):

        print(
            f"{index:<5}"
            f"{receipt.get('id', 'N/A'):<10}"
            f"{receipt.get('title', 'N/A')[:18]:<20}"
            f"{receipt.get('filename', 'N/A')[:33]:<35}"
            f"{receipt.get('date', 'N/A'):<15}"
        )

    print("=" * 100)


# ==========================================================
# SEARCH RECEIPT
# ==========================================================

def search_receipt(username):

    receipts = load_data(RECEIPT_FILE)

    if not receipts:

        print("\n❌ No receipts found.")
        return

    user_receipts = [
        receipt
        for receipt in receipts
        if receipt.get("username") == username
    ]

    if not user_receipts:

        print("\n❌ You have no receipts.")
        return

    print("\n" + "=" * 60)
    print("                  🔍 SEARCH RECEIPT")
    print("=" * 60)

    keyword = input(
        "Enter title or receipt ID: "
    ).strip().lower()

    if not keyword:

        print("\n❌ Search value cannot be empty.")
        return

    results = []

    for receipt in user_receipts:

        receipt_id = receipt.get("id", "").lower()
        title = receipt.get("title", "").lower()

        if keyword in receipt_id or keyword in title:

            results.append(receipt)

    if not results:

        print("\n❌ No matching receipts found.")
        return

    print("\n" + "=" * 100)
    print("                    🔍 SEARCH RESULTS")
    print("=" * 100)

    for receipt in results:

        print(f"Receipt ID : {receipt.get('id', 'N/A')}")
        print(f"Title      : {receipt.get('title', 'N/A')}")
        print(f"File       : {receipt.get('filename', 'N/A')}")
        print(
            f"Description: "
            f"{receipt.get('description', 'N/A')}"
        )
        print(f"Date       : {receipt.get('date', 'N/A')}")
        print(f"Time       : {receipt.get('time', 'N/A')}")

        print("-" * 60)


# ==========================================================
# DELETE RECEIPT
# ==========================================================

def delete_receipt(username):

    receipts = load_data(RECEIPT_FILE)

    if not receipts:

        print("\n❌ No receipts found.")
        return

    user_receipts = [
        receipt
        for receipt in receipts
        if receipt.get("username") == username
    ]

    if not user_receipts:

        print("\n❌ You have no receipts.")
        return

    print("\n" + "=" * 90)
    print("                    🗑️ DELETE RECEIPT")
    print("=" * 90)

    print(
        f"{'No':<5}"
        f"{'ID':<10}"
        f"{'Title':<25}"
        f"{'Date':<15}"
    )

    print("-" * 90)

    for index, receipt in enumerate(user_receipts, start=1):

        print(
            f"{index:<5}"
            f"{receipt.get('id', 'N/A'):<10}"
            f"{receipt.get('title', 'N/A')[:23]:<25}"
            f"{receipt.get('date', 'N/A'):<15}"
        )

    print("-" * 90)

    # ------------------------------------------------------
    # Select Receipt
    # ------------------------------------------------------

    while True:

        try:

            choice = int(
                input("Enter Record Number to Delete: ")
            )

            if 1 <= choice <= len(user_receipts):
                break

            print("\n❌ Invalid Record Number.")

        except ValueError:

            print("\n❌ Please enter a valid number.")

    selected_receipt = user_receipts[choice - 1]

    # ------------------------------------------------------
    # Show Selected Receipt
    # ------------------------------------------------------

    print("\nSelected Receipt")
    print("-" * 40)

    print(
        f"ID          : "
        f"{selected_receipt.get('id')}"
    )

    print(
        f"Title       : "
        f"{selected_receipt.get('title')}"
    )

    print(
        f"File        : "
        f"{selected_receipt.get('filename')}"
    )

    print(
        f"Description : "
        f"{selected_receipt.get('description')}"
    )

    print("-" * 40)

    # ------------------------------------------------------
    # Confirmation
    # ------------------------------------------------------

    confirm = input(
        "\nAre you sure you want to delete? (Y/N): "
    ).strip().lower()

    if confirm != "y":

        print("\nℹ️ Delete Operation Cancelled.")
        return

    # ------------------------------------------------------
    # Delete Physical File
    # ------------------------------------------------------

    file_path = selected_receipt.get("path")

    if file_path and os.path.isfile(file_path):

        try:

            os.remove(file_path)

        except OSError:

            print(
                "\n⚠️ Receipt file could not be deleted."
            )

    # ------------------------------------------------------
    # Delete JSON Record
    # ------------------------------------------------------

    receipts.remove(selected_receipt)

    save_data(RECEIPT_FILE, receipts)

    print("\n✅ Receipt Deleted Successfully!")


# ==========================================================
# RECEIPT MANAGEMENT
# ==========================================================

def receipt_management(username):

    while True:

        choice = receipt_menu()

        if choice == "1":

            upload_receipt(username)

        elif choice == "2":

            view_receipts(username)

        elif choice == "3":

            search_receipt(username)

        elif choice == "4":

            delete_receipt(username)

        elif choice == "5":

            break