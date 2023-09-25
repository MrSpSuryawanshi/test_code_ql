import sys
import json

def custom_code_scanner(file_path):
    # Apne custom code scanning rules ko yahan apply karein
    # Example: Aap eval() aur exec() jaise functions ko search kar sakte hain
    
    issues = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_number = 1
        
        for line in lines:
            if 'eval(' in line or 'exec(' in line:
                issues.append({
                    "message": "Potential security issue found",
                    "location": {
                        "path": file_path,
                        "positions": {
                            "begin": {
                                "line": line_number,
                                "column": line.index('eval(') if 'eval(' in line else line.index('exec(')
                            }
                        }
                    }
                })
            line_number += 1
    
    return issues

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python custom_scanner.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    issues = custom_code_scanner(file_path)
    
    results = {
        "version": "2.1.0",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "Custom Code Scanner",
                    "version": "1.0.0"
                }
            },
            "results": issues
        }]
    }
    
    with open("sarif-results.sarif", "w") as sarif_file:
        json.dump(results, sarif_file)

    print(f"SARIF results saved to sarif-results.sarif")
