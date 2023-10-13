import os

def find_eval_exec_files(path):
    """
    `eval()` और `exec()` का उपयोग करने वाली सभी फ़ाइलों की एक सूची लौटाता है,
    जिसमें `.min.js` फ़ाइलें शामिल नहीं हैं।

    Args:
        path: खोजने के लिए शुरू करने के लिए पथ।

    Returns:
        `eval()` और `exec()` का उपयोग करने वाली फ़ाइलों की एक सूची,
        जिसमें `.min.js` फ़ाइलें शामिल नहीं हैं।
    """

    files = []  # खाली सूची बनाई जाती है जिसमें फ़़ाइलों का पथ संग्रहीत होगा

    for root, _, filenames in os.walk(path):
        # `os.walk()` का उपयोग दिए गए पथ के तहत सभी फ़ोल्डरों और फ़ाइलों को खोजने के लिए किया जाता है
        for filename in filenames:
            # हर फ़ाइल के लिए
            file_path = os.path.join(root, filename)
            # फ़ाइल का पूरा पथ तैयार किया जाता है

            if filename.endswith(".min.js"):
                # `.min.js` फ़ाइलों को छोड़ दिया जाता है
                continue

            with open(file_path, encoding="utf-8") as f:
                # फ़ाइल खोली जाती है और स्रोत कोड पढ़कर उसे `source` नामक वेरिएबल में संग्रहित करता है
                source = f.read()

            if "eval(" in source or "exec(" in source:
                # अगर स्रोत कोड में "eval(" या "exec(" होता है, तो वह फ़ाइल का पथ सूची में जोड़ दिया जाता है
                files.append(file_path)

    return files

if __name__ == "__main__":
    # यदि स्क्रिप्ट सीधे चलाया जाता है (और नहीं एक आवश्यकता है गाइड GitHub क्रिया नियोक्ता के लिए)
    files_using_eval_exec = find_eval_exec_files("app.py")

    # फ़ाइलों की सूची प्रिंट करें
    for file_path in files_using_eval_exec:
        print(f"File uses eval() or exec(): {file_path}")
