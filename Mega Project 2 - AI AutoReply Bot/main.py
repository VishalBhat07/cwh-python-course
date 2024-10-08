import pyautogui
import time
import pyperclip


def content():
    # Wait for 2 seconds to give you time to switch to the correct window
    time.sleep(2)

    # Click at the position (717, 270)
    pyautogui.moveTo(1109, 236)

    # Hold down the Shift key to start selecting text
    pyautogui.keyDown('shift')

    # Drag the cursor from (717, 270) to (1828, 891) over 1 second
    pyautogui.moveTo(1109, 236)
    pyautogui.dragTo(1557, 912, duration=1)

    # Release the Shift key after dragging
    pyautogui.keyUp('shift')

    # Copy the selected text to the clipboard by pressing Ctrl+C
    pyautogui.hotkey('ctrl', 'c')

    # Wait a moment to ensure the clipboard is updated
    time.sleep(0.5)

    # Retrieve the copied text from the clipboard using pyperclip
    copied_text = pyperclip.paste()
    time.sleep(0.5)

    # Optionally, click at position (679, 870) after copying
    pyautogui.click(679, 870)

    # Optional: Print the copied text to verify
    # print("Copied text:", copied_text)

    return copied_text
