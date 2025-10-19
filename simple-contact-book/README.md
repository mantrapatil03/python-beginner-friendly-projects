<h1 align="center"> Contact Book (Python)</h1>

<p align="center">
A simple, class-based <b>Contact Book</b> application built with Python.  
Store and manage contact information (name & phone number) directly from the terminal. 
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Platform-Terminal-orange?style=for-the-badge&logo=windowsterminal"></a>
  <a href="https://github.com/mantrapatil03/python-beginner-friendly-projects/stargazers"><img src="https://img.shields.io/badge/Stars-GitHub-yellow?style=for-the-badge&logo=github"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative"></a>
</p>

##  Features
- Add new contacts
- Store multiple contacts
- Display all saved contacts in a clean format

---

##  How It Works
1. Each contact is represented by the `Contact` class.
2. All contacts are stored inside the `ContactBook` class.
3. You can add new contacts using `add_contact()` and display them with `show_contacts()`.


---

##  Example Usage
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

##  Output:
```python
Name: Shree, Phone: 123-456-7890
Name: Ram, Phone: 987-654-3210
```


##  Author

Made with ❤️ by **Mantra Patil**

💼 LinkedIn: https://www.linkedin.com/mantrapatil25

✉ techmantrapatil@gmail.com

<h3 align="center">⭐ If you found this project useful, give it a star on GitHub! ⭐</h3> <p align="center"> <img src="https://img.shields.io/badge/Keep%20Organizing%20%26%20Coding-Python-blue?style=for-the-badge&logo=python"> </p>
