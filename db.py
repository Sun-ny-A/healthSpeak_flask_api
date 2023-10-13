#temp db for testing initial routes

doctors = {
  '1':{
    'doctor_name':'Albert Lopez, MD',
    'specialization':'Family Medicine',
    'email':'alopez@email.com',
    'phone_number':'773.999.9999',
    'accepting_patients':'YES',
    'profile_bio':'A Chicago native, Dr. Albert Antonio Lopez has been serving the community for 25 years...',
    'password':'111'
  },
  '2':{
    'doctor_name':'John legend, MD',
    'specialization':'Cardiothoracic Surgeon',
    'email':'jlegendz@email.com',
    'phone_number':'773.888.8888',
    'accepting_patients':'NO',
    'profile_bio':'Also an avid pianist, Dr. John Legend...',
    'password':'222'
  },
   '3':{
    'doctor_name':'Zendaya Coleman, MD, PhD',
    'specialization':'Pediatric Surgeon',
    'email':'zcoleman@email.com',
    'phone_number':'773.777.7777',
    'accepting_patients':'YES',
    'profile_bio':'One of the most prominent in the region...',
    'password':'333'
   }
}

users = {
  '1':{
    'username':'Andre3000',
    'first_name':'Andre',
    'last_name':'Outkast',
    'email':'outkast@email.com',
    'password':'444'
  },
  '2':{
    'username':'MrPresi',
    'email':'presi@email.com',
    'first_name':'Flying',
    'last_name':'Eagle',
    'password':'555'
  },
  '3':{
    'username':'WonderWoman',
    'email':'wonder@email.com',
    'password':'666'
  },
  '4':{
    'username':'Superman',
    'email':'super@email.com',
    'password':'777'
  },
  '5':{
    'username':'Batman',
    'email':'bat@email.com',
    'first_name':'Bruce',
    'last_name':'Wayne',
    'password':'888'
    },
  '6':{
    'username':'StormTrooper',
    'first_name':'Yoda',
    'last_name':'Hater',
    'email':'storm@email.com',
    'password':'999'
  }
}

questions = {
  '1':{
    'forum_question':'Is all chest pain worrisome?',
    'user_id':'1',
    'doctor_id':'1',
    'forum_responses':'Most chest pain is benign—that is, not caused by heart or lung disease. Mostly it is a musculoskeletal issue. If the pain comes when you take a deep breath, or you feel short of breath with walking or a feeling of “heaviness” in your chest, you should seek immediate medical attention.'
  },
  '2':{
    'forum_question':'I hate physicals, do I really have to go every year?',
    'user_id':'3',
    'doctor_id':'1',
    'forum_responses':'Many diseases are preventable. Seeing a doctor who knows your body and what is normal for you can help to identify changes and what might be emerging health problems. Your blood pressure, fasting labs and any other tests that your doctor sees fit will help to prevent future illness. As Benjamin Franklin once said, “An ounce of prevention is worth a pound of cure.'
  },
  '3':{
    'forum_question':'My child needs surgery but I\'m terrified to let them go through with it. How do I know if it\'s really necessary?',
    'user_id':'6',
    'doctor_id':'3',
    'forum_responses':'Being frightened for your child is an understandable and normal repsonse. The decision to perform surgery is not one that any surgeon takes lightly and we make sure the benefits of the surgery outweigh the risks. Have you gotten a second opinion? I also recommend reaching out to your child\'s surgeon and voicing any concerns you may have.'
  }
}

answers = {
  '1':{
    'forum_response':'Most chest pain is benign—that is, not caused by heart or lung disease. Mostly it is a musculoskeletal issue. If the pain comes when you take a deep breath, or you feel short of breath with walking or a feeling of “heaviness” in your chest, you should seek immediate medical attention.',
    'user_id':'1',
    'doctor_id':'1',
    'patient_question':'Is all chest pain worrisome?'
  },
  '2':{
    'forum_response':'Many diseases are preventable. Seeing a doctor who knows your body and what is normal for you can help to identify changes and what might be emerging health problems. Your blood pressure, fasting labs and any other tests that your doctor sees fit will help to prevent future illness. As Benjamin Franklin once said, “An ounce of prevention is worth a pound of cure.',
    'user_id':'3',
    'doctor_id':'1',
    'patient_question':'I hate physicals, do I really have to go every year?'
  },
  '3':{
    'forum_response':'Being frightened for your child is an understandable and normal repsonse. The decision to perform surgery is not one that any surgeon takes lightly and we make sure the benefits of the surgery outweigh the risks. Have you gotten a second opinion? I also recommend reaching out to your child\'s surgeon and voicing any concerns you may have.',
    'user_id':'6',
    'doctor_id':'3',
    'patient_question':'My child needs surgery but I\'m terrified to let them go through with it. How do I know if it\'s really necessary?'
  }
}

# content for question/answer https://www.rxsaver.com/blog/most-common-health-questions 