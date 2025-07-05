# 🧹 Extract Clean HTML From URL For Elementor

This Python script helps you extract and clean the main content from a WordPress page or blog post. It's specifically designed to remove bloated HTML, inline styles, and unnecessary tags — making the content Elementor-ready.

---

## ✨ What It Does

- ✅ Fetches a live WordPress page (using its URL)
- ✅ Finds the main content area (`.entry-content`, `<article>`, or `<main>`)
- ✅ Cleans the HTML to keep only essential text-based tags
- ✅ Keeps only the `href` attribute for links
- ✅ Outputs a lightweight, readable HTML file

---

## 🛠 Required Libraries

Install using pip:

```
pip install requests beautifulsoup4
```

- **`requests`** – For making HTTP requests to fetch the page  
- **`beautifulsoup4`** – For parsing and cleaning the HTML content

---

## 🔖 Allowed Tags & Attributes

### ✅ Allowed Tags

Only the following HTML tags are preserved:

```
allowed_tags = ['p', 'strong', 'b', 'i', 'em', 'a', 'ul', 'ol', 'li', 'br']
```

> Any tag not in this list is removed, but its inner text content remains.

### ✅ Allowed Attributes

- Only `href` is allowed on `<a>` tags.
- All other attributes (like `class`, `style`, `id`) are stripped.

---

## 📁 Output

- The cleaned HTML is saved to a file: `lightweight.html`
- You can safely copy-paste this into **Elementor's Text Editor**, **Icon List**, or **HTML widget**

---

## 💡 Example Use Case

> You’re migrating content from an old WordPress blog to a new Elementor-based site and want to keep only the essential, clean HTML — without messy inline styles or bloated wrappers.

---

## 🔗 Example URL

```
url = "https://academyatthelakes.org/parent-portal/25-26-summer-checklist/"
```

Replace with any WordPress content page URL.

---

## ✅ Done!

Run the script and get Elementor-ready HTML in seconds. No extra formatting needed.
