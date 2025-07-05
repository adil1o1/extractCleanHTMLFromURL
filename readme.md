# 🧹 Extract Clean HTML From URL For Elementor

This Python script helps you extract and clean HTML content from any webpage — especially WordPress sites built with **Elementor**. It removes all bloated wrappers, headers, footers, inline styles, and unnecessary tags, giving you clean, paste-ready HTML for Elementor widgets.

---

## ✨ What It Does

- ✅ Fetches a live page using its URL
- ✅ Strips out `<header>` and `<footer>` content entirely
- ✅ Extracts only what’s inside `<body>`
- ✅ Removes all tags except the essential text-based ones
- ✅ Keeps only the `href` attribute on `<a>` tags
- ✅ Saves the cleaned output as `lightweight.html`
- ✅ Copies the HTML directly to your clipboard

---

## 🛠 Required Libraries

Install using pip:

```bash
pip install requests beautifulsoup4 pyperclip
```

- `requests` – For making HTTP requests  
- `beautifulsoup4` – For parsing and cleaning HTML  
- `pyperclip` – For copying cleaned HTML to your clipboard

---

## 🔖 Allowed Tags & Attributes

### ✅ Allowed Tags

Only the following tags are preserved:

```python
allowed_tags = ['a', 'br', 'p', 'ul', 'ol', 'li', 'b', 'strong', 'i', 'em', 'u']
```

All other HTML tags are removed, but their inner text is retained.

### ✅ Allowed Attributes

Only:

```python
<a href="...">Link</a>
```

- All other attributes (`class`, `id`, `style`, etc.) are stripped.

---

## 📁 Output

- Clean HTML is saved as: `simpleHTMLText.html`
- It's also automatically copied to your clipboard
- Paste it directly into:
  - Elementor **Text Editor**
  - **Icon List**
  - Or even a **Custom HTML widget**

---

## 💡 Example Use Case

You’re copying content from an old WordPress blog or school page into a modern Elementor-based layout. This script strips out all unwanted styling, containers, and scripts — keeping only clean content you can paste and style in Elementor.

---

## ✅ You're Done!

Run the script. Get Elementor-ready HTML in seconds. No more editing messy code manually.

---
