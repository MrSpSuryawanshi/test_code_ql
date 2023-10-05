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

  files = []
  for root, _, filenames in os.walk(path):
    for filename in filenames:
      file_path = os.path.join(root, filename)

      # Skip `.min.js` files.
      if filename.endswith(".min.js"):
        continue

      with open(file_path, encoding="utf-8") as f:
        source = f.read()

      if "eval(" in source or "exec(" in source:
        files.append(file_path)

  return files
