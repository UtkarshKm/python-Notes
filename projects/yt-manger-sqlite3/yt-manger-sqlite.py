import sqlite3
con = sqlite3.connect("yt-manger.db")

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, time TEXT NOT NULL)")

def list_all_videos():
    cur.execute("SELECT * FROM videos")
    print("\n")
    print( "*" * 20, "All Videos", "*" * 20)
    print("\n")
    for row in cur.fetchall():
        # (1, 'new test', '4 Hr')
        print(f"{row[0]}. Name : {row[1]}, Duration : {row[2]}")
        
    print("\n")

def add_video():
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video():
    list_all_videos()
    try:
        index = int(input("Enter the index of the video to update: "))
        
        # Check if the ID exists in the database
        cur.execute("SELECT id FROM videos WHERE id = ?", (index,))
        if cur.fetchone():
            name = input("Enter the new name of the video: ")
            time = input("Enter the new time of the video: ")
            cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, index))
            con.commit()
            print("Video updated successfully!")
        else:
            print("Invalid index - video not found")
    except ValueError:
        print("Please enter a valid number")

def delete_video():
    list_all_videos()
    try:
        index = int(input("Enter the index of the video to delete: "))
        
        # Check if the ID exists in the database
        cur.execute("SELECT id FROM videos WHERE id = ?", (index,))
        if cur.fetchone():
            cur.execute("DELETE FROM videos WHERE id = ?", (index,))
            con.commit()
            print("Video deleted successfully!")
        else:
            print("Invalid index - video not found")
    except ValueError:
        print("Please enter a valid number")

def main():
    while True:
        print("\nYoutube Manager | choose an option:")
        print("1. list all videos")
        print("2. add a video")
        print("3. update a video")
        print("4. delete a video")
        print("5. exit")
        
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case _:
                print("Invalid choice")
                continue
            
    con.close()

if __name__ == "__main__":
    main()