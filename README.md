# Pokemon Instagram OpenCV border

Add a 200px whitespace border to the card in order to prevent forced cropping on Instagram. 

[https://www.instagram.com/coffeewin_/](https://www.instagram.com/coffeewin_/)

## Usage

Put all `.jpg` card images inside the same directory as the `add_border.py` script then run the script. 

```
python add_border.py
```

Alternatively, you can run the `add_border_to_card.exe` binary executable. It will create a `/done` directory with all the processed cards inside. 

Command to create `.exe`

```
pyinstaller --onefile --windowed --name="add_border_to_card" --icon="pikachu_face.ico" .\add_border.py
```

## Result

Before `->` After

![](docs/example.png)
