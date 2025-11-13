import sys

def main():
    if len(sys.argv) != 4:
        raise ValueError("Incorrect number of arguments is given")
    else:
        mode = sys.argv[1]
        text = sys.argv[2]
        shift = validate(text, mode, sys.argv[3])
        result = (caesar(mode, text, shift))
        print(result)

              
def validate(text, mode, shift):
    if mode not in ['encode', 'decode']:
        raise ValueError("invalid mode. Use 'encode' или 'decode'.")
    for char in text:
        if ord(char)>127:
            raise ValueError("The script does not support your language yet")
    try:
        shift = int(shift)
        return shift
    except ValueError:
        print('Error: Shift must be integer')
        sys.exit(1)

def caesar(mode, text, shift):
    result = []
    if mode == 'decode':
        shift = -shift

    for char in text:
        if char >= 'A' and char <= 'Z':
            new_char = chr((ord(char)-ord('A') +shift) %26 + ord('A'))
            result.append(new_char)
        elif char >= 'a' and char <= 'z':
            new_char = chr((ord(char)-ord('a') +shift) %26 + ord('a'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
        
if __name__ == '__main__':
    main()