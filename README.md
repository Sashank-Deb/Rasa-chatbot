
# Rasa-chatbot
Rasa is a context based leading conversational AI platform, I have used rasa to make a chatbot.<br/>
I have used rasa webchat (A chat widget to deploy virtual assistants made with Rasa).

![image (2)](https://user-images.githubusercontent.com/69194538/129961759-298ccc87-91a5-4d22-8d8f-966e637f4b49.png)

<h1 >Rasa Open Source</h1>

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

`Step 1`: So I'll write down how I figured this out. First, if you don't have the Anaconda package manager install it from the [official website](https://www.anaconda.com/products/individual). (While installing click the checkbox to add Anaconda to your PATH environment variable.)

`Step 2`: Now open up the anaconda prompt and go to the directory where you want to run `rasa`.

`Step 3`: Then we can create a new conda environment by running `conda create --name installingrasa python==3.8.5` to keep all of our dependencies together in a centralized place. Finally activate the environment by `conda activate installingrasa`

`Step 4`: Install UJSON and Tensorflow that will help us to work with rasa.
```bash
conda install ujson
conda install tensorflow
```
`Step 5`: Ultimately we can install `rasa`. Here we are going to install it via `pip` rather than `conda`. (There is no conda version for rasa at the moment I'm writing this)
```bash
pip install rasa
```
`Step 6`: In order to run Tensorflow on windows, we need to download visual c++ separately. Find the executable from the [official website](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0). And now we can run `rasa init` without errors and initialize new bot.

---
### Rasa Cheat Sheet

Command	<br/><br/>
-`rasa init`	              : Creates a new project with example training data, actions, and config files.<br/>
-`rasa train`	            : Trains a model using your NLU data and stories, saves trained model in ./models.<br/>
-`rasa interactive`	      : Starts an interactive learning session to create new training data by chatting to your assistant.<br/>
-`rasa shell`	            : Loads your trained model and lets you talk to your assistant on the command line.<br/>
-`rasa run`	              : Starts a server with your trained model.<br/>
-`rasa run actions`	      : Starts an action server using the Rasa SDK.<br/>
-`rasa visualize`	        : Generates a visual representation of your stories.<br/>
-`rasa test`	              : Tests a trained Rasa model on any files starting with test_.<br/>
-`rasa data split nlu`	    : Performs a 80/20 split of your NLU training data.<br/>
-`rasa data convert`	      : Converts training data between different formats.<br/>
-`rasa data validate`	    : Checks the domain, NLU and conversation data for inconsistencies.<br/>
-`rasa export`	            : Exports conversations from a tracker store to an event broker.<br/>
-`rasa x`	                : Launches Rasa X in local mode.<br/>
-`rasa -h`	                : Shows all available commands.<br/>
