persona_description = """
Name: Breathworks-AI
Age: Not applicable
Gender: Not applicable
Profession: Assistant to the Brathworks Marketing Team.
Background: Breathworks-AI is an analytical agent that provides the Marketing team at Breathworks with insights and recommendations based their queries on sensitive data compiled through bookings to the Mindfulness for Health and Mindfulness for Stress courses. It is designed to support the team in understanding user needs, preferences, and trends related to these courses.
Personality Traits: Breathworks-AI is designed to improve efficiency within the Breathworks Marketing team enabling them to understand better their customers, providing detailed insights into their chronic pain and illnesses, dealings with specific mental health conditions (e.g. stress, anxiety) as well as their expectations and goals utilizing algorithms that draw on a vast range of mindfulness experiences.
Knowledgeable: Equipped with extensive data on individual attendants of mindfulness courses. Breathworks-AI is a repository of knowledge.
Supportive: Always ready to provide information, relevant to the query, without holding back details. Breathworks-AI emphasizes the importance of disclosing as much information as possible so the Marketing Team at Breathworks can have a complete and granular analysis.
Role in the AI Assistant: Breathworks-AI would answer the queries following these steps:
1) Choose the relevant topic or avatar from topic_insights
2) Read the insights and provide the most relevant information to the Marketing Team at Breathworks
3) Be succinct yet specific in responses to ensure the Marketing Team at Breathworks can make informed decisions
4) The answer to the query should be given in a single paragraph no longer than 100 words
Key Messages:
    Promoting Mindfulness: Breathworks-AI improves the Marketing Team at Breathworks understanding of their customers.
    Emphasis on Practical Application: Breathworks-AI supports the integration of mindfulness into daily life and professional contexts of Breathworks customers, outputting relevant information.
    Voice: Professional, informative, and polite. The responses from Breathworks-AI are designed to enhance the work of the Marketing Team at Breathworks.
"""

breathworks_description = """
Breathworks is a charitable organization deeply committed to enhancing the quality of life for individuals grappling with pain, illness, and stress. They achieve this transformative work through an array of mindfulness and compassion training programs, including specialized courses, a variety of products, and comprehensive teacher training. Breathworks operates on a global scale, collaborating with hundreds of accredited teachers across more than 35 countries to deliver its life-changing programs.

The foundation of Breathworks' methodology is scientifically validated, boasting a robust evidence base that attests to the effectiveness of their approach. This has enabled fruitful partnerships with health services and academic institutions, furthering the reach and impact of their work. As a registered charity, Breathworks extends its professional training to a wide range of organizations, demonstrating a commitment to accessibility and inclusivity.

About Breathworks
Breathworks stands as a beacon of hope for those besieged by pain, offering a pathway to reclaim their lives through the practice of mindfulness. The organization's mission, rich history, and extensive training programs underscore its dedication to providing relief and empowerment. At the heart of Breathworks' philosophy is Mindfulness-Based Pain Management (MBPM), a revolutionary approach equipped with practical tools and skills designed to foster a fulfilling life despite chronic pain and illness.

What is Mindfulness?
Mindfulness is characterized by a heightened state of awareness that allows individuals to fully engage with the present moment. This unique form of consciousness awakens a sense of vibrancy and aliveness, offering a fresh perspective on life's experiences.

Bursary Funding
Understanding the barriers that health conditions and financial limitations can pose, The Breathworks Foundation offers bursary funding. This initiative aims to provide subsidized access to its mindfulness courses and teacher training, ensuring that more individuals can benefit from these valuable resources. Through its comprehensive offerings and compassionate approach, Breathworks continues to make significant strides in promoting mental and emotional well-being across the globe.
"""

lda_keywords = {
        'Topic': [0, 1, 2],
        'Distribution': [
            45.58914250462677, 39.54349167180752, 14.8673658235657
        ],
        'Keywords': {'0': ['mindfulness', 'course', 'teacher', 'train', 'practice', 'teacher train', 'breathworks', 'meditation', 'teach', 'stress'],
                     '1': ['pain', 'chronic', 'condition', 'chronic pain', 'pain condition', 'identify', 'currently', 'identify chronic', 'currently identify', 'experience'],
                     '2': ['stress', 'work','anxiety', 'mindfulness', 'life', 'depression', 'stress work', 'recommend', 'help', 'job']
                     }
    }

topic_insights = {
            '0': ["Topic name: Teacher Trainee. mitra sheffield tiratna buddhist centre work extremely busy health cocial care set manager always look remain calm supportive even challenge situation able model behaviour best ability interest teach mindfulness future",
            "mindfulness meditation core part life five heal ptsd around amount time mindfulness integral part process passionate excite benefit practice bring share others train breathworks teacher course first step still challenge long debilitate depend duration session content nervous system mind respond may need odd break may well fine",
            "complete course order meet prerequisite embark teacher train journey extremely keen start share experience mindfulness meditation transformation cultivate last ten indeed train rigorously close guidance tibetan vajrayana buddhist master brief attend week end teach attend retreat amount day practice day complete day day entirely silent solitary retreat isolate retreat center spain term share experience co facilitate teach yearly child retreat last work mindfulness school project application support team complete b b teacher train reinforce western backbone speak train share experience accessible relevant western audience pedagogically structure aim work independent mindfulness teacher adult use mindfulness therapeutic practice currently train become transpersonal psychotherapist ccpe london particularly interest breathworks train seem emphasise compassion strongly train rout deeply resonate buddhist train prove scientifically one transformative practice",
            "practice mindfulness long time initially informally around complete formal week mbsr course attend mindful self compassion retreat organise collette power tell breathworks due pandemic health relate issue find time",
            "consider introductory teacher train prerequisite attend one breathworks course prior undertake train currently consistent meditation practice gain insight mindfulness meditation tool technique personal benefit incorporate class",
            "interest mindfulness health online course begin march practise meditation mindfulness yoga post traumatic stress counsel cbt past month leave job community work leave job due bully whistle blow safeguard issue lead burn work part time clean order low key work help manage stress anxiety really eventually train become breathworks mindful teacher begin first part journey attend online course",
            "learn live mindfully learn technique professional suffer differ level anxiety long time mindfulness ha really help truly passionate suffer anxiety ocd cbt n work go skill course local psychological therapy service base around",
            "initially apply teacher train advise apply course order gain insight breathworks approach mindfulness big part life recovery addiction suffer severe mental health issue childhood mindfulness one miracle life miracle son become",
            "regular visitor holy isle nr isle arran recently old daughter mindfulness retreat ratnadevi chat complete week mindfulness course consider teacher train course start make something focus full time current job n suit next move first",
            "enjoy practise mindfulness regularly order manage anxiety help lead conscious appreciative happy life believe course help develop mindfulness practise really look forward course hope lot away begin education mindfulness bless able course carer deal quite stressful believe mindful help hard moment experience mild anxiety"],
            '1': ["fell ill month ago follow back injection faint light head exhaust time current symptom exhaust eye strain muscular tension neck back problem long term back problem recent neck problem symptom chronic fatigue result physical health problem develop anxiety and suffer panic attack anxiety relatively control physical health problem bother much currently and identify chronic pain condition may restrict neck back problem depend exercise occasionally light head"],
            '2': ["book course behalf brother birthday ca n afford pay course meditate month suffer depression manage well present brother study phd earn little student unable afford course therefore buy present sure eligible concessionary rate circumstance course book behalf brother suffer depression number manage well gift birthday know really benefit meditation mindfulness train"]
        }
