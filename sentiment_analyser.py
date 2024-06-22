import tkinter as tk
from tkinter import messagebox
import joblib
import re
import requests



def predict(text):
    model = joblib.load('sentiment_analysis_svm_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    X = vectorizer.transform([text])
    y_pred = model.predict(X)[0]
    return y_pred

def get_sentiment():
    positive = 0
    neutral = 0
    negative = 0

    print("Process Initiated....")

    for comment in comments:
        if predict(comment) == 1:
            positive += 1
        elif predict(comment) == 0:
            neutral += 1
        else:
            negative += 1

    positive = (positive / len(comments)) * 100
    negative = (negative / len(comments)) * 100
    neutral = (neutral / len(comments)) * 100

    print(f"positive:{positive}, negative:{negative}, neutral:{neutral}")
    print("Process Completed..")
    return positive, negative, neutral

comments = [
    "Last part is a must watch",
    "Boss: We want to build a todo app.",
    "Dev: Okay, I'll just need these 18 frameworks.",
    "Let's go with AWS to give us the most complicated user experience.",
    "I'm glad Fireship thinks so, too. I thought I was just bad at it.",
    "2yrs later ... This video still makes sense ... Grateful for this...",
    "Perhaps I'm still too old school, but back in the days of BDD (behavior-driven development) we had the rule:  Vision first, features second, specs third, tools fourth!  Which means: Only when we all agree on our vision of our project, we can pin down the features we want to implement. Only when we all agree on the features of the project, we can specify how we want to implement them. Only when we all agree on the specifications (specs) we can look for the best technologies to get the job done. I still believe in this approach. Can't help it.",
    "Bro you're actually fluent in trash-talk XD The passive aggressive sarcasm is absolute fire",
    "And that ladies and gentlemen, are the requirements for a junior developer.",
    "This video is written like an award-winning novel. It's got a compelling storyline complete with the suffocating dread as we get bombarded with a seemingly endless amount of unfamiliar names and colorful logos which then climaxes when we throw it all out and start from scratch ultimately ending with a satisfying conclusion. A perfect 5/7",
    " If you don't build a good experience at first, you'll never get to the point where you'll need something like Kubernetes  I love this quote",
    "As a developer, this video has me laughing and crying at the same time until the last section where everything got simplified and half the team lost their jobs, haha.",
    "Six years ago I had an idea and I started to build it. I quickly fell into the stack rabbit hole described perfectly in this video. Then I took a regular job and put that project on hold, until now. I’m really focused on keeping things simple this time and I loved this video!!",
    "Omg, dude, you're a genius. Every video you make just proves how well you understand those stuff...No one can explain those topics better than you.",
    "This is fucking brilliant. “Let’s go with AWS because we want an overly complicated interface” lmao",
    "Stacks was made to lessen the code, now configuring a stack is more complicated than writing the code",
    "Before this video, I was watching all the videos for every front and back-end tech stack, and it was making me sleepy. Thank you, fireship for this video and for rejuvenating me.",
    "Bro, please never stop doing these videos. They have literally gotten me through college, and most of my work experience come from videos just like yours.",
    "I never comment on videos, but you sir deserve some recognition, not only have I learned with you, but I also just straight up love binging your videos!",
    "“More code lead to a better quality app” the humor never stops  also i liked the bigger video. 100s is too little",
    "“You’ll never get to the point where you actually need Kubernetes”  brilliant as usual",
    "I have to say, one of the most useful videos I've ever watched . As a newbie I feel a lot less overwhelmed",
    "Amazing break down of what I've been looking for for months as a newbie. Thanks for simplifyng things in a condensed way",
    " AWS for the most complicated user experience' LOL",
    "I've lived my professional life from the beginning to now dumping unfinished side projects left and right, but it hasn't clicked for me until I read the title of this video why do I tend to do that, it's over engineering and overall planning. A todo app build on a 10 layer stack will not change the world, I should plan just the right amount and save more energy for actually realizing the project and completing it.",
    "Your videos are so awesome! I had literally come to the conclusion of the vue-fire stack TODAY, in my quest for elegant simplicity. Was unaware of petite, but will probably stick with the more complicated vue.",
    "I usually don't like to watch much web dev stuff on YouTube because i find its often filled with way too much hype and over engineering, basically everything you demonstrated in this video",
    "Your videos are a breath of fresh air!",
    " It's impossible to make CSS look good on its own, so we're going to bring in Tailwind  i'm crying",
    "The stack might be petite fire but this video is mega fire!",
    "I found this very informative! In my personal experience, if there's more than one person involved with the coding, adding Github + GH Actions for the convenience wouldn't be too much of an extra stretch but you're right if it's just you doing your own thing and don't mind manually handling it.",
    "No video has ever discouraged me more about writing an application",
    "Man, the  pick your poison  slide killed me You really never disappoint on quality Phenomenal content as usual!",
    "Me for 9 mins:  Damn, I must be trash.  Also me:  THEEEEERRRREEEEE you go ",
    "This is a great video! Thank you for that :) I'm just beginning to learn from my colleagues and from podcasts about all these technologies, and this video brings it all together, in a way that makes sense to me. Thanks again!",
    "thank u!!! im graduating with a cs degree and i cant believe nobody has ever explained what each of these stack does. this is the first video ive seen that actually differentiates them!!!",
    "You are a genuine out-of-the-box thinker. Your videos are short yet densely packed with information, both technically and philosophically. Fireship is like a breath of fresh air. Awesome!",
    "Jeff, in under 12 minutes, you’ve eliminated 200 thousand Million BILLION tech careers…. good going, dear  … all the best to you, Cheers!",
    "Manual deployment may work for small applications built by just a handful of engineers. But as soon as you have multiple teams building upon code that was written by other people, and all of it must play nicely together, and you have an active user base that you dont want to risk disrupting with outages, the packaging and deployment processes get more complex and more critical. And frankly, they become a lot more of a pain in the ass, and can require more developer time being spent going through the motions. And that time is expensive.",
    "As someone with non IT background and into business analyst, it gives a very good bird's-eye view and context to the whole orchestral",
    " now it's time to switch gears to the hard part, the back end  ouch, my poor fragile front end heart",
    "Even though I do this type of stuff all day everyday for like 10 years now. This video made me realize how stupidly insane all these tools and technologies have gotten.",
    "First introduce popular tech landscape, then simplify it down to what should be focused by the beginners. Great content!",
    "As a coder for 20+ years this hits hard I hurts to know how many of these frameworks I've used and still use in the tech stacks I work with daily.",
    "And for all you young punks out there, the OG stack LAMP is STILL runnin' the block!",
    "mevn can be rearranged to venm and all of a sudden it's the coolest stack acronym. throw in something that starts with an O and you have the full effect. VENOM",
    "Lol, this is awesome. You literally listed every 'hey let's add every bit of bullshit into this, to make it impossible to debug' new technology that I've ever hated to have to deploy on a site. Literally wish you were in every meeting I've had to sit through with devs who can't figure out the shiny new tech that they wanted to add in so they don't have to write the 12 lines of code that would have saved the 3 hours it took just to get the environment setup, so that they could be confused by the syntax.",
    "The last part of the video was pure joy, with just Firebase and React I was able to deliver a web and mobile app for a client in no time, for the record before that the tech stack looked pretty similar to the start of the video it was freaking overwhelming, the lesson here is tech stack should be chosen after business needs are well understood",
    "9:00 AWS deep learning dk detection capabilities. Awesome Nice one Jeff",
    "This is by far one of the best videos I have ever seen stating exactly what NOT to do lol. Overengineering is a wormhole I fell into many times in my early days as a developer. Luckily, I just use K.I.S.S. now... Not necessarily a webstack rather than a frame of mind.  Keep It Simple, Supid  :-)",
    "You wouldn't believe the catharsis I felt when the music started playing and he started showing how to do this more simply. I felt so relieved knowing that I wasn't stupid for not knowing every single thing in the over-engineered stack.",
    "This was amazingly educational for any new web dev to see the whole picture. Thank you!",
    "Over-engineering a website? Write the frontend in WASM without using the DOM, the backend in C because performance, duh, and create your own shitty database because you don't like any.",
    "This video is the perfect mix of good information and top notch trolling at the same time. Love it.",
    "I love that his humor is so subtle. Like he says the thing and it takes you a second to realize he was trolling, lol",
    " It’s a must that our app can’t handle more than 100 concurrent users so let’s use AWS . Thanks for speaking the truth"
]

