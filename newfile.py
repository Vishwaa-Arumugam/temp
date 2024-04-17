import requests
import base64

repo_owner = "Vishwaa-Arumugam"
repo_name = "temp"
branch_name = "main"

# 9287

for i in range(117, 9287):
    file_path = f"extracted_frames/frame_{i}.jpg"
    file_path2 = f"extracted_frames{i//1000}/frame_{i}.jpg"

    with open(file_path, "rb") as f:
        image_content = f.read()

    image_base64 = base64.b64encode(image_content).decode()

    token = "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"

    commit_payload = {
        "message": "Add image file",
        "content": image_base64,
        "branch": branch_name,
    }

    api_url = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path2}"
    )
    headers = {"Authorization": f"token {token}"}
    response = requests.put(api_url, headers=headers, json=commit_payload)
    print(response.status_code)
    if response.status_code == 201:
        print("Image uploaded successfully.")
    else:
        print("Failed to upload image.")
