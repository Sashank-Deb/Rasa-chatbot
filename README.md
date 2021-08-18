# Rasa-chatbot
Rasa is a context based leading conversational AI platform, I have used rasa to make a chatbot
<h1 align="center">Rasa Open Source</h1>



<a href="https://grnh.se/05a908c02us" target="_blank"><img align="center" src="https://www.rasa.com/assets/img/github/hiring_banner.png" alt="An image with Sara, the Rasa mascot, standing next to a roadmap with future Rasa milestones: identifying unsuccessful conversations at scale, continuous model evaluation, controllable NLG and breaking free from intents. Are you excited about these milestones? Help us make these ideas become reality - we're hiring!" title="We're hiring! Learn more"></a>

<hr />

<img align="right" height="244" src="https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png" alt="An image of Sara, the Rasa mascot bird, holding a flag that reads Open Source with one wing, and a wrench in the other" title="Rasa Open Source">

### Rasa is an open source machine learning framework to automate text-and voice-based conversations. With Rasa, you can build contextual assistants on:
- Facebook Messenger
- Slack
- Google Hangouts
- Webex Teams
- Microsoft Bot Framework
- Rocket.Chat
- Mattermost
- Telegram
- Twilio
- Your own custom conversational channels

Rasa helps you build contextual assistants capable of having layered conversations with
lots of back-and-forth. In order for a human to have a meaningful exchange with a contextual
assistant, the assistant needs to be able to use context to build on things that were previously
discussed – Rasa enables you to build assistants that can do this in a scalable way.

There's a lot more background information in this
[blog post](https://medium.com/rasa-blog/a-new-approach-to-conversational-software-2e64a5d05f2a).

---
- **What does Rasa do ?**
  [Check out the Website](https://rasa.com/)

- **If you are new to Rasa**
  [Get Started with Rasa](https://rasa.com/docs/getting-started/)

- **Read the detailed docs**
  [Read The Docs](https://rasa.com/docs/)

- **Learn how to use Rasa**
  [Tutorial](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)

- **Have a question ?**
  [Rasa Community Forum](https://forum.rasa.com/)

---
### Rasa installation guide

`Step 1`: So I'll write down how I figured this out. First, if you don't have the Anaconda package manager install it from the official website. (While installing click the checkbox to add Anaconda to your PATH environment variable.)

`Step 2`: Now open up the anaconda prompt and go to the directory where you want to run rasa.

`Step 3`: Then we can create a new conda environment by running conda create --name installingrasa python==3.8.5 to keep all of our dependencies together in a centralized place. Finally activate the environment by conda activate installingrasa

`Step 4`: Install UJSON and Tensorflow that will help us to work with rasa.
```bash
conda install ujson
conda install tensorflow
```
`Step 5`: Ultimately we can install rasa. Here we are going to install it via pip rather than conda. (there is no conda version fr rasa at the moment I'm writing this)

pip install rasa
`Step 6`: In order to run Tensorflow on windows, we need to download visual c++ separately. Find the executable from the official website. And now we can run rasa init without errors and initialize new bot.
