## 📒 Contact Book (Python)

A simple **Contact Book** application built with Python classes.  
It lets you store contact information (name & phone number) and display saved contacts.  

---

## 🚀 Features
- Add new contacts
- Store multiple contacts
- Display all saved contacts in a clean format



---

## 🛠️ How It Works
1. Each contact is represented by the `Contact` class.
2. All contacts are stored inside the `ContactBook` class.
3. You can add new contacts using `add_contact()` and display them with `show_contacts()`.


---

## 💻 Example Usage
```python
from contact_book import Contact, ContactBook

# Create a new contact book
contact_book = ContactBook()

# Add contacts
contact_book.add_contact(Contact("Shree", "123-456-7890"))
contact_book.add_contact(Contact("Ram", "987-654-3210"))

# Show contacts
contact_book.show_contacts()
```

## 🖥️ Output:
```python
Name: Shree, Phone: 123-456-7890
Name: Ram, Phone: 987-654-3210
```

## 📌 Future Improvements


Save contacts permanently (using JSON/CSV/Database)

Search & delete contacts

Update existing contacts

Simple command-line or GUI interface

## 🏷️ Author

Made with ❤️ by Mantra Patil 

🌐 GitHub: https://github.com/mantrapatil03

💼 LinkedIn: https://www.linkedin.com/mantrapatil25

✉ techmantrapatil@gmail.com






