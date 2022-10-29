from pytube import *

def playlist(option,location):

	url = input("Enter the Url: ")

	playlist = Playlist(url)

	while True:
		try:
			playlist = Playlist(url)
			if (len(playlist.video_urls) is not 0):
				break
		except:
			continue

	print(f'Number of videos in playlist: {len(playlist.video_urls)}')

	if option==1:
		playlist.download_all()

	elif option==2:
		for video_url in playlist.video_urls:
			print("\n	Downloading: ",video_url)
			i=0
			while True:
				i+=1
				try:
					YouTube(video_url).streams.filter(audio_only=True)[-1].download(location)
				except:
					cont = input("\n	an error occured, try again? (y/n)\n 	")
					if cont=="y":
						continue
					elif cont=="n":
						break

def video(option,location):
	url = YouTube(input("Enter the Url: "))
	if option == 1:
		url.streams.get_highest_resolution().download(location)
	elif option == 2:
			url.streams.filter(only_audio=True)[-1].download(location)


def main():
	option1 = input("What do you want to download: \n[1] Video \n[2] Playlist\n:")
	option2 = input("Do you want it to be Audio or Original: \n[1] Original \n[2] Audio\n:")
	location = input("\nWhere do you want your files too be save: ")
	if option1 == "1":
		if option2 == "1":
			video(1,location)
		elif option2 == "2":
			video(2,location)
	elif option1 == "2":
		if option2 == "1":
			playlist(1,location)
		elif option2 == "2":
			playlist(2,location)

main()
