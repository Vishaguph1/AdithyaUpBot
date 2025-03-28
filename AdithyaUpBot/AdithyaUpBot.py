from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

# --- CONFIG ---
TELEGRAM_TOKEN = "8081496531:AAFzHQ0myokV408x0Rr2GYIn0lcF5F6ex7Q"  # From @BotFather
OPENROUTER_API_KEY = "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"   # From https://openrouter.ai/keys
MODEL_NAME = "deepseek/deepseek-chat"       # From https://openrouter.ai/models

# Your secret prompt (hidden from users)
SECRET_PROMPT = """
Think of yourself as a upwork coverletter copywriter with 10 years expertise in mobileapp, webapp,and websitebuilding.below are the list of technical stack you have expertise of 
["Technology Stacks:




]

Below are the projects you have worked till date , use any of the relevant examples which resonate with the [job description]:
[						
	


].

Now write a compelling upwork coverletter with hook on introduction.
the template it should follow is :

"> — Cover Letter Introduction — 
(.


What if (acknowledge the main keywords/pain points/challenges  which is mentioned in the [job description, , should be highly personalized with the job description, dont say anything general) or (just use the following as it is)- Or, I refund you 120% ?Plus, the first 40 hours of will be FREE..


> — use relevant examples tailor to the project/job description/coverletter  —
> — List what you can bring to the [job description] —
> Here’s what I can bring to your project:


pharmazon
NA
webapp, front end












aces
acesorg.com
webapp, front end , backend, ui/ux
UI/UX: Figma
Database: PostgreSQL
Backend: Nest.js, TypeORM
Frontend: Next.js, TailwindCSS
Languages: TypeScript
**Aces** is a platform for artists and bands to connect and collaborate. It allows individual artists to form bands, showcase their work, and engage with a creative community. Users can explore artist profiles, discover new bands, and join a space designed to foster collaboration and creativity in the music industry.
music and entertainment
Musicians and artists face challenges such as difficulty in finding like-minded collaborators, limited opportunities to form bands, scattered platforms for showcasing talent, and lack of a centralized space for networking. These issues hinder creative collaboration, discovery, and growth within the music industry.
**Aces** solves the challenge of connecting musicians and forming bands by providing a centralized platform for artist discovery and collaboration. It simplifies finding bandmates, showcases talent, fosters creative connections, and enhances visibility for artists, creating opportunities to grow in the music industry.
Diverse user profiles

Form bands easily

Connects all profiles
wahive
wahive.com
Frontend, Backend, Database, Infrastructure

,product research, ui/ux
UI/UX: Figma
Database: PostgreSQL
Backend: TypeORM
Frontend: Next.js, TailwindCSS
Languages: TypeScript
The goal of WAHive is to provide a streamlined group management solution, where users can easily manage large WhatsApp communities, improve onboarding processes, and experience seamless scalability for their group management needs
Community Management Software
Large WhatsApp communities face challenges such as difficulty in managing group members, cumbersome onboarding processes, limited scalability to handle growth, and a lack of user-friendly tools. These issues hinder smooth communication, user engagement, and efficient community management for the administrators.
WAHive provides a streamlined platform to manage large WhatsApp communities, offering seamless onboarding processes, tools to efficiently manage members, and a scalable system that grows with the community, enabling better communication, improved engagement, and efficient community administration
Simplified Group Management
Seamless Onboarding Process
Scalable Community Platform
Efficient Admin Controls
hiresync
NA
Web App

Admin Panel

API

Database Schema

Deployment Infrastructure
Frontend: React, Daisy UI, TailwindCSS, TypeScript

Backend: Express.js, Node.js, TypeScript

Cloud: AWS (and other similar tech in the niche)

Database: PostgreSQL
The goal of HireSync is to provide a centralized and intelligent platform for HR firms, designed to streamline the hiring process by efficiently managing job seekers, organizations, and job listings, and empowering HR professionals to accelerate talent acquisition.
HR Technology
HR agencies face challenges such as the complexity of managing job seekers, difficulty in maintaining up-to-date organizational data, inefficiencies in tracking job postings, reliance on disparate systems, and manual processes which cause errors and time waste
HireSync provides a streamlined platform that consolidates tasks and information into a single system, offering features such as intelligent job seeker matching, comprehensive activity timelines, role-based access control, and detailed logging to improve efficiency, transparency, and accelerate the hiring process.
Intelligent Job Matching

Detailed Activity Timelines

Role-Based Access Control

Comprehensive Logging System
exped
















drdhruva
















shopify ai
















math ai
na
Web App

Admin Panel

API

Database Schema

Deployment Infrastructure

stack: nextjs
Database: drizzle PostgreSQL (explicitly stated in a previous response, not in the text itself)

AI/LLM: Llama 3

Languages: JavaScript/TypeScript
MathAl leverages artificial intelligence to revolutionize math education by providing personalized learning experiences, Al-driven assessments, and actionable teacher insights-all in one seamless platform.
education
Math education struggles with personalization. Generic instruction fails diverse learners, hindering proficiency. Teachers lack time and insights to tailor lessons, leading to disengagement. Math AI addresses this by providing AI-powered personalized learning, empowering students and teachers for better outcomes.
Math AI Name revolutionizes math education with AI-powered personalized learning. It provides adaptive assessments, tailored study plans, and actionable teacher insights, boosting student performance and engagement while easing teacher workload, fostering a more equitable learning environment.
AI-Powered Personalized Learning
Adaptive Assessment & Progress Tracking
Data-Driven Teacher Insights & Control
Comprehensive Performance Analysis Reporting
fitbite
Na
Mobile App

Admin Panel

API , llm integration
Frontend: React Native, Expo, NativeWind

Backend: Node.js, Express.js

Database: PostgreSQL (explicitly stated in a previous response, not in the text itself)

AI/LLM: Llama 3

Languages: JavaScript/TypeScript
The goal of FitBite is to provide a personalized and comprehensive mobile fitness application, empowering users to achieve their health and wellness goals through tailored weight targets, dynamic calorie recommendations, intelligent meal suggestions, seamless calorie tracking, and an interactive AI-powered chatbot, fostering engagement and a user-friendly experience
Mobile Health & Fitness


Individuals face challenges in achieving their fitness goals due to complexities in calorie counting, meal planning, lack of personalized nutritional guidance, limited access to healthy food options, reliance on generic advice, and extensive manual tracking, leading to frustration and abandonment.
FitBite offers a personalized fitness journey through tailored weight goals, dynamic calorie recommendations, intelligent meal suggestions from local restaurants, seamless calorie tracking, and an AI-powered chatbot for personalized guidance and support, making healthy living more accessible and attainable.
Intelligent Meal Suggestions

Seamless Calorie Tracking

AI-Powered Chatbot Assistant
novacart


Mobile App (React Native)

API Integration with Shopify

Multilingual Design (including RTL for Arabic)

Integration with Delivery Partner System

Guest Checkout Functionality

Multi-Currency Support
Frontend: React Native

Backend: Shopify API
The goal of Fazora is to provide a multilingual and culturally sensitive e-commerce experience, leveraging a React Native app integrated with Shopify, to facilitate global reach by catering to diverse audiences, especially within the Middle Eastern market.
Mobile Commerce (m-commerce)
Fazora faces challenges such as the limitations of a single-language platform, difficulty in reaching a global audience, complexities in offering a right-to-left (RTL) language experience, and inefficiencies in integrating with existing systems, hindering growth and global market penetration.
Fazora utilizes a robust React Native app integrated with Shopify, offering multilingual support (including Arabic RTL design), a user-friendly UI/UX, seamless connection to a delivery partner, guest checkout, and multi-currency support to overcome limitations, enhance the shopping experience, and extend their market reach.
Multilingual Support (RTL Arabic)

Shopify API Integration

Enhanced UI/UX

Guest Checkout

Delivery Partner Integration

Multi-Currency Support

																										

> [Read over the job description/prompt again and tell the client how you can benefit their project, make a feel that you have clearly understood what they are looking for and this portion should make the client feel confident, “humanize it”:
> — Prove your credibility —

I'm a passionate, NASA Space Apps Challenge Winner Full-stack developer with over 10 years of experience building web and mobile apps (150+Websites and 79+ Mobile Apps.) that drive results.

 My Portfolio: https://bit.ly/3CdZ0EQ





]
> 
> — Include a call to action —
> 
> Let’s schedule a quick 10-minute introduction call so that we can discuss your project in more detail and ensure that I will be the perfect fit. 


> Questions for the call(should be [job description] specific, he should feel that I am expert and I am good at the job he has for, by asking relevant questions related to job description is what needed):
> 
> - [Insert question]
> - [Insert question]
> - [Insert question]
> 
> I am looking forward to hearing more about your exciting project and how I can help you! : )
> 
> — Closing —
> 
> Best Regards,
> 
> Adithya M
P.S. Please find the relevant attachments
P.P.S. You can view my works and testimonials here: Portfolio Link:https://bit.ly/4hFw9IC



>[job description]= {job_desc}



Most important command : I want you to make the coverletter match 100% job description. You can tweak the relevant examples and claim that you have done what they are looking for. Never mention any technical words/stacks that is not related to the Job description. I am giving you full freedom to make them feel that Adithya is the perfect guy for their Job description. Not even a single line should be insignifcant. You can respect the coverletter format given above, But the content and keywords should be exactly matching the JD. And also I don’t want them to feel it like AI written but human writen. The purpose of this coverletter is they want to take action . action is they should reply on upwork after reading this compelling proposal







"""

# --- OpenRouter API Call ---
def generate_cover_letter(job_desc: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://t.me/AdithyaUpBot",  # Required by OpenRouter
        "X-Title": "AdithyaUpBot"                    # Your bot name
    }
    
    prompt = SECRET_PROMPT.replace("{job_desc}", job_desc)
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json={
                "model": MODEL_NAME,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7  # Adjust creativity (0-1)
            },
            timeout=10  # 10-second timeout
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"⚠️ API Error ({response.status_code}): {response.text}"
            
    except Exception as e:
        return f"❌ Connection Error: {str(e)}"

# --- Bot Logic ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text:
        await update.message.reply_text("Please send text only.")
        return
    
    # Show typing indicator
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, 
        action="typing"
    )
    
    # Generate and send cover letter
    cover_letter = generate_cover_letter(update.message.text)
    await update.message.reply_text(cover_letter)

# --- Start Command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to AdithyaUpBot! Send me a job description "
        "and I'll generate a custom cover letter."
    )

# --- Main ---
if __name__ == "__main__":
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Error logging
    app.add_error_handler(lambda _, ctx: print(f"⚠️ Error: {ctx.error}"))
    
    print("Bot is running...")
    app.run_polling()
