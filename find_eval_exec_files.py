import os

def find_eval_exec_files(path):
  """
  `eval()` और `exec()` का उपयोग करने वाली सभी फ़ाइलों की एक सूची लौटाता है।

  Args:
    path: खोजने के लिए शुरू करने के लिए पथ।

  Returns:
    `eval()` और `exec()` का उपयोग करने वाली फ़ाइलों की एक सूची।
  """

  files = []
  for root, _, filenames in os.walk(path):
    for filename in filenames:
      file_path = os.path.join(root, filename)
      with open(file_path) as f:
        source = f.read()

      if "eval(" in source or "exec(" in source:
        files.append(file_path)

  return files


def main():
  path = os.getcwd()
  files = find_eval_exec_files(path)
  for file in files:
    print(file)


if __name__ == "__main__":
  main()
