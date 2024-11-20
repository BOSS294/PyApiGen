
# API Key Generator

A modern and secure **API Key Generator** built with **PyQt5**. This application allows users to generate customizable and secure API keys with various filters for enhanced security. The tool is designed with a sleek, dark-themed UI and provides a seamless experience for developers to quickly generate API keys with ease.

## Features

### 1. **Customizable Key Filters**
   - **Key Length**: Choose the desired length of the API key (from 8 to 64 characters).
   - **Include Numbers**: Option to include numeric characters in the API key.
   - **Include Uppercase Letters**: Option to include uppercase letters.
   - **Include Lowercase Letters**: Option to include lowercase letters.
   - **Include Special Characters**: Option to include special characters (`!@#$%^&*` etc.).
   - **Remove Ambiguous Characters**: Option to exclude visually similar characters such as `l`, `I`, `O`, `0` to avoid confusion.

### 2. **Generate API Key**
   - Generate a secure API key based on user-selected filters.
   - Key generation is completely random, ensuring a high level of security.

### 3. **Copy to Clipboard**
   - Once the API key is generated, you can easily copy it to the clipboard with a single click.
   - The application logs every action, so you can track generated keys and copied keys.

### 4. **Logs Section**
   - A **logs section** at the bottom of the UI shows activity in real-time, such as key generation and copy actions.
   - Logs are displayed in a clean green color, providing a professional look and feel.

### 5. **Clean & Modern UI**
   - The user interface is built with **PyQt5**, featuring a dark theme with white text for better contrast.
   - The sidebar provides key metadata about the application, including:
     - Developed on
     - Last updated
     - Version number
     - Developer's name
     - Special thanks to contributors
     - Instructions on how to use the tool

---

## Installation

To run this project locally, you'll need **Python** and **PyQt5** installed. Here's how to set it up:

### Prerequisites
- Python 3.x
- PyQt5 library

---

## Usage

1. Launch the **API Key Generator** application.
2. In the **API Key Filters** section, select your desired options:
   - Set the key length.
   - Choose whether to include numbers, uppercase letters, lowercase letters, and special characters.
3. Click the **Generate API Key** button.
4. Once the key is generated, it will appear in the text box.
5. Click the **Copy Key** button to copy the API key to your clipboard.
6. Check the **Logs** section for real-time updates about the key generation process.

---

## Future Enhancements

While this application is fully functional, here are some **future enhancements** that could be implemented to improve its functionality and user experience:

1. **Advanced Encryption Option**:
   - Add an option to encrypt the generated API key using various algorithms (e.g., AES) before displaying it.

2. **Save API Keys**:
   - Allow users to save generated API keys to a local file or a database for future use.

3. **User Authentication**:
   - Implement user authentication (sign-up/sign-in) for a more personalized experience.
   - This would be useful for keeping track of generated API keys by users.

4. **API Key Expiration**:
   - Add an expiration date for the generated API keys. Users could specify when their API keys should expire, and the application could alert them when it’s time to regenerate the key.

5. **Multi-Language Support**:
   - Add support for multiple languages to cater to users worldwide.

6. **API Integration**:
   - Implement an API that allows users to generate API keys directly from a web application or from a REST API.

7. **Enhanced Key Customization**:
   - Allow for more advanced customization of the key generation process (e.g., specific character sets, prefixes, and suffixes).

---

## Screenshots

![image](https://github.com/user-attachments/assets/c6ac3002-fc55-4d0f-aad2-e3767dd7be57)


---


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

- **Developed by:** Mayank Chawdhari
- **GitHub:** [Mayank Chawdahri](https://github.com/BOSS294)
- **Email:** mayankchawdhari@gmail.com

---
