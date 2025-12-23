# Hardware design
In this folder, all the details of the hardware project will be stored.

## Create a physical token showing a QR code that links to a Github page.

- [x] Create new repository folder and identify the link.
- [x] Create the QR code image with identified link.
  - Check [QR.io](https://qr.io/) and [MiniQR](https://mini-qr-code-generator.vercel.app/).
  - Modify manually if necessary.
- [x] Save `svg` and `png` files needed for PCB and gerbers.
- [x] Create new Kicad project for PCB.
- [x] Order PCB @ [JLC PCBs](https://cart.jlcpcb.com/quote?plateType=1).
- [x] Wait...
- [x] Enjoy 😎


#### Reminders:
- QR code also works upside down, therefore I could have mirrored 25 logo so that lace would come from top left instead of bottom right.
- Do not drill inside finder patterns otherwise QR does not work.
- Do not have exposed copper QR otherwise QR does not work.

