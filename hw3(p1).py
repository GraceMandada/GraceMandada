data_list=["And now here is my secret, a very simple secret: It is only with the heart that one can see rightly; what is essential is invisible to the eye.",
"All grown-ups were once children... but only few of them remember it.",
"People have forgotten this truth,\" the fox said. \"But you mustn’t forget it. You become responsible forever for what you’ve tamed. You’re responsible for your rose.",
"It is the time you have wasted for your rose that makes your rose so important.",
"The most beautiful things in the world cannot be seen or touched, they are felt with the heart.",
"What makes the desert beautiful,' said the little prince, 'is that somewhere it hides a well...",
"You - you alone will have the stars as no one else has them...In one of the stars I shall be living. In one of them I shall be laughing. And so it will be as if all the stars were laughing, when you look at the sky at night...You - only you - will have stars that can laugh.",
"Well, I must endure the presence of a few caterpillars if I wish to become acquainted with the butterflies.",
"You see, one loves the sunset when one is so sad.",
"You're beautiful, but you're empty...One couldn't die for you. Of course, an ordinary passerby would think my rose looked just like you. But my rose, all on her own, is more important than all of you together, since she's the one I've watered. Since she's the one I put under glass, since she's the one I sheltered behind the screen. Since she's the one for whom I killed the caterpillars (except the two or three butterflies). Since she's the one I listened to when she complained, or when she boasted, or even sometimes when she said nothing at all. Since she's my rose.",
"If you love a flower that lives on a star, it is sweet to look at the sky at night. All the stars are a-bloom with flowers...",
"And when your sorrow is comforted (time soothes all sorrows) you will be content that you have known me. You will always be my friend. You will want to laugh with me. And you will sometimes open your window, so, for that pleasure . . . And your friends will be properly astonished to see you laughing as you look up at the sky! Then you will say to them, 'Yes, the stars always make me laugh!' And they will think you are crazy. It will be a very shabby trick that I shall have played on you...",
	"You become responsible, forever, for what you have tamed."]
query=input("query:")
print(query)
for i,quote in enumerate(data_list):
	found_at = quote.lower().find(query.lower())
	if( found_at >= 0):
		print("Found at ", i, "..."+quote[found_at:found_at+50], "...")