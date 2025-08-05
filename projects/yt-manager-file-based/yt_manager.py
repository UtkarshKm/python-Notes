import json


def load_data():
    try:
        with open("youtube.txt", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as f:
        json.dump(videos, f, indent=2)

def list_all_videos(videos):
    print("\n")
    print( "*" * 20, "All Videos", "*" * 20)
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name : {video['name']}, Duration : {video['time']}")
    print("\n")
        

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the name of the video: ")
        time = input("Enter the time of the video: ")
        videos[index-1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index")

def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager | choose an option:")
        # list all videos, add, update, delete, exit
        print("1. list all videos")
        print("2. add a video")
        print("3. update a video")
        print("4. delete a video")
        print("5. exit")
        
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video( videos)
            case "5":
                break
            case _:
                print("Invalid choice")
                continue
            
if __name__ == "__main__":
    main()
