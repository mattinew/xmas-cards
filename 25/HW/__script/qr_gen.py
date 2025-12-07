import qrcode
from PIL import Image

# 1. CONFIGURATION PARAMETERS
#--------------------------------------------------------------------------------
# YOUR LINK OR TEXT TO ENCODE
data = 'https://mattinew.github.io/xmas-cards/25/SW/'

# Path to the logo file (should be .png with transparency, if possible)
logo_path = 'qr_logo.png' 

# Output filename
output_filename = "qr_code.png"

# Error correction level:
# M (Medium - 15%) | Q (Quartile - 25%) | H (High - 30%)
# We use 'Q' or 'H' for adding a large or non-central logo
ECL = qrcode.constants.ERROR_CORRECT_Q 

# 2. BASE QR CODE CREATION
#--------------------------------------------------------------------------------
box_size = 10
border = 4
qr = qrcode.QRCode(
    # Version: Keep None to automatically choose the minimum size
    version=None,
    # Error correction level
    error_correction=ECL,
    # Size of each "square" of the QR code in pixels
    box_size=box_size, 
    # Border thickness (white squares around the code)
    border=border, 
)
qr.add_data(data)
qr.make(fit=True)

# Create the QR code image. Background color is White, modules are Black
qr_img = qr.make_image(fill_color="white", back_color="black").convert('RGB')

# 3. LOGO LOADING AND RESIZING
#--------------------------------------------------------------------------------
try:
    logo = Image.open(logo_path).convert("RGBA")
except FileNotFoundError:
    print(f"Error: Logo file not found at path: {logo_path}")
    exit()

# Calculate the maximum size for the logo (e.g., 25% of the QR size)
qr_size = qr_img.size[0] - 2*border*box_size  # Actual QR code size without border
max_logo_size = int(qr_size * 0.25)

# If the logo is too large, resize it while maintaining proportions
ratio = min(max_logo_size / logo.width, max_logo_size / logo.height)
new_logo_size = (int(logo.width * ratio), int(logo.height * ratio))
logo = logo.resize(new_logo_size)

# 4. POSITION CALCULATION (BOTTOM RIGHT)
#--------------------------------------------------------------------------------
# Calculate the coordinates for the top-left corner of the logo
logo_w, logo_h = logo.size

# Offset margin from the borders (e.g., 20 pixels to avoid extreme borders and the Alignment Pattern)
offset = 10

# Calculate (x, y) coordinates to position the logo at the bottom right
# x_start: total width - logo width - offset
x_start = qr_size - logo_w - offset + border*box_size
# y_start: total height - logo height - offset
y_start = qr_size - logo_h - offset + border*box_size

# 5. OVERLAY AND SAVING
#--------------------------------------------------------------------------------
# Paste the logo onto the QR code using a mask for transparency
# (logo, box=tuple, mask=logo)
qr_img.paste(logo, (x_start, y_start), logo)

# Save the final QR code
qr_img.save(output_filename)

print(f"QR code successfully generated: {output_filename}")
print(f"Correction Level: Q (25%).")
print(f"Logo positioned at: ({x_start}, {y_start})")
print("DO NOT forget to test the scan!")