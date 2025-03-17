







# import requests
# import m3u8
# from flask import Flask, render_template, request, redirect, flash, jsonify, session, make_response,  redirect, url_for


# chunk_size = 256

# # url = "https://dood.li/d/btoyb4saguzi"
# url = "https://www.youtube.com/watch?v=p07ZZZVL72E"

# # r = requests.get(url, stream=True)
# r = requests.get(url)
# m3u8_master = m3u8.loads(r.text)
# type(m3u8_master)

# playlist_url = m3u8_master.data['playlists']
# r = requests.get(playlist_url)
# playlist = m3u8.loads(r.text)
# print(playlist.data)


# # fsal = open('holaxd.html','w')
# # print("123")
# # # fsal.write(str(r.text))
# # fsal.write(jsonify(r.text))
# # fsal.close()




# # print(r.text)
# # jsonify(r.text)




# # m3u8.model.M3U8

# # print(m3u8_master.data)



# # with open("lynda.mp4" , "wb") as f:
# #   for chunk in r.iter_content(chunk_size=chunk_size):
# #     f.write(chunk)







# #  from pytube import YouTube
 
# # url = '''
# # https://youtube.com/shorts/fsNhuk1l6aA?si=r2oNIplE7R-NW1SZ
# # '''

# # def Download(link):
# #   yt = YouTube(link)
# #   aaa = yt.streams.get_highest_resolution()
# #   try:
# #     aaa.download()
# #   except Exception as e:
# #     print("Hubo un error al descargar el video del URL proporcionado... ",e)
# #   print("¡Descarga completada con éxito!")
   
# # # Pedimos al usuario en la línea de comandos ingresar el URL del video para descargar
# # # link = input("xdxdd")
 
# # # Descargamos el video
# # Download(url)

