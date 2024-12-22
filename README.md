# picodulce-themes
The official repository of the picodulce launcher themes

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nixietab/picodulce-themes/.github%2Fworkflows%2Fcreate_repository.yml)


# How to create themes?

### **1. Understand the Theme Structure**

A theme typically includes 4 simple parts:

-   **Manifest Information:** Metadata about the theme (name, description, author, license).
-   **Palette Configuration:** Defines the colors used in the UI.
-   **Background Image (Optional):** A background image for the main page of the launcher
-   **Stylesheet instructions (Optional):** A group of css-like styling [Qt Documentation](https://doc.qt.io/qt-6/stylesheet-syntax.html)


Here is a example:

    {
      "manifest": {
        "name": "Dark",
        "description": "The default picodulce launcher theme",
        "author": "Nixietab",
        "license": "MIT"
      },
      "palette": {
        "Window": "#353535",
        "WindowText": "#ffffff",
        "Base": "#191919",
        "AlternateBase": "#353535",
        "ToolTipBase": "#ffffff",
        "ToolTipText": "#ffffff",
        "Text": "#ffffff",
        "Button": "#353535",
        "ButtonText": "#ffffff",
        "BrightText": "#ff0000",
        "Link": "#2a82da",
        "Highlight": "#4bb679",
        "HighlightedText": "#ffffff"
      },
      "stylesheet": "",
      "background_image_base64": ""
    }

### **2. Creating the Manifest**
The manifest provides essential details about your theme to appear on the repository, It should look something like this:


#### **Recommendations:**

-   Keep the name concise but descriptive.
-   Write a short, clear description (e.g., "A cute vanilla theme inspired by Nekopara").
-   If sharing publicly, use an open license like MIT or Apache 2.0.

### **3. Designing the Color Palette**

The palette determines the theme's visual identity. Each key in the palette corresponds to an element in the UI. Here's an explanation of the keys:

| **Key**            | **Description**                              | **Example Value** |
|---------------------|----------------------------------------------|-------------------|
| `Window`           | Background color of the main window.                        | `"#31363b"`       |
| `WindowText`       | Text color inside the main window.                          | `"#ffffff"`       |
| `Base`             | Background color of input fields.                           | `"#191919"`       |
| `AlternateBase`    | Alternating background for lists.                           | `"#31363b"`       |
| `ToolTipBase`      | Tooltip background color.                                   | `"#ffffff"`       |
| `ToolTipText`      | Tooltip text color.                                         | `"#ffffff"`       |
| `Text`             | General text color.                                         | `"#ffffff"`       |
| `Button`           | Background color of buttons and tabs.                       | `"#31363b"`       |
| `ButtonText`       | Button and tabs text color.                                 | `"#ffffff"`       |
| `BrightText`       | Highlighted or warning text.                                | `"#ff0000"`       |
| `Link`             | Hyperlink text color.                                       | `"#2a82da"`       |
| `Highlight`        | Highlight color for selected items and play button          | `"#2a82da"`       |
| `HighlightedText`  | Text color for selected items.                              | `"#ffffff"`       |


#### **Color Design Recommendations**
    
1.  **Maintain Contrast:** Ensure that text and background colors have enough contrast for readability.
    
2.  **Use a Consistent Color Palette:**
    
    -   Tools like [Coolors](https://coolors.co) can help you generate cohesive color palettes.
    -   Try **monochromatic** or **complementary** color schemes for a harmonious look.
 

### Adding Background Images
You can include a background image in your theme by embedding it as a Base64 string in the `background_image_base64` field of the JSON file.

#### Requirements for the Image
- **Format:** The image must be in plain Base64 encoding (no headers like `data:image/png;base64,`).
- **Dimensions:** The image should be exactly **400x320 pixels** for optimal display.
- **Encoding:** Use a tool like [Base64 Guru](https://base64.guru/converter/encode/image) to encode your image.





Disclaimer:
I do not own most of the multimedia content used in these themes. All credits are given to the respective authors and creators. If any content belongs to you and you'd like it to be properly attributed or removed, please contact me.
