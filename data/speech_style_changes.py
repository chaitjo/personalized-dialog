import numpy as np

def read_babi(fname):
    lines = []
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    dialogs = []
    dialog = []
    for line in lines:
        if len(line) == 1:
            dialogs.append(dialog) 
            dialog = []
            continue
        # line = line[line.find(' ')+1:-1]
        # line = line.split('\t')
        # dialog.append(line)
        dialog.append(line[line.find(' ')+1:-1].split('\t'))
    return dialogs
    
    
def process_utterence(utterence):
    patterns = ['api_call', 'what do you think of this option:', 'here it is']
    for pattern in patterns:
        if pattern in utterence:
            return(pattern, utterence.split(pattern)[1])
    return (utterence, '')
        
    
def modify_babi(dialogs, utterences):
    new_dialogs = []
    for dialog in dialogs:
        temp_dialog_set = [[['male young']],[['female young']],[['male middle-aged']],[['female middle-aged']],[['male elderly']],[['female elderly']]]
        for turn in dialog:
            if len(turn) > 1:
                temp_turn = []
                pattern, data = process_utterence(turn[1])
                for i, modified_response in enumerate(utterences[pattern]): # change this to patterns
                    temp_turn = [turn[0], modified_response + data]
                    temp_dialog_set[i].append(temp_turn)
            else:
                for i in range(len(temp_dialog_set)):
                    temp_dialog_set[i].append(turn)
        for temp_dialog in temp_dialog_set:
            new_dialogs.append(temp_dialog)
    return new_dialogs
    

def save_babi(dialogs, fname, shuffle=False):
    if shuffle:
        np.random.shuffle(dialogs)
    with open(fname, 'w', encoding='utf-8') as f:
        for dialog in dialogs:
            for i, line in enumerate(dialog):
                if len(line) == 2:
                    f.write(str(i) + ' ' + line[0] + '\t' + line[1] + '\n')
                else:
                    f.write(str(i) + ' ' + line[0] + '\n')
            f.write('\n')

            
def modify_candidates(fname, utterences):
    # candidates = ['male young', 'female young', 'male middle-aged', 'female middle-aged', 'male elderly', 'female elderly']
    candidates = []
    with open(fname, 'r', encoding='utf-8') as f:
        candidates = f.readlines()
    new_candidates = []
    for candidate in candidates:
        candidate = candidate.split('1 ')[1][:-1]
        pattern, data = process_utterence(candidate)
        for modified_response in set(utterences[pattern]):
            new_candidates.append('1 ' + modified_response + data)
    return new_candidates
    

def save_candidates(candidates, fname, shuffle=False):
    if shuffle:
        np.random.shuffle(candidates)
    with open(fname, 'w', encoding='utf-8') as f:
        for candidate in candidates:
            f.write(candidate+'\n')

    
if __name__ == '__main__':
    utterences = {
        "hello what can i help you with today" : ("hey dude what is up", 
            "hey girl how is it going", 
            "hello sir what can i help you with", 
            "hello maam how can i help you", 
            "greetings sir what may i assist you with today", 
            "good day madam how could i assist you today"),
        
        "i'm on it" : ("i'm on your request", 
            "be right back with your reservation", 
            "i'm processing the request", 
            "give me a second for processing the reservation", 
            "excellent sir i will start the request now", 
            "thank you madam i shall start the reservation now"),
        
        "any preference on a type of cuisine" : ("what food are you looking for", 
            "what food are you looking for", 
            "what type of cuisine would you like to eat", 
            "what type of cuisine would you like to eat", 
            "may i know your preference on the type of cuisine", 
            "could you tell me your preference on the type of cuisine"),
        
        "where should it be" : ("where should it be",
            "where should it be",
            "where should it be located",
            "where should it be located",
            "may i know where the restaurant should be located"
            "could you tell me where the restaurant should be located"),
    
        "which price range are looking for" : ("what should the price be",
            "what should the price be",
            "which price range are you looking for",
            "which price range are you looking for",
            "may i know your prefered price range",
            "would you mind telling me your price range"),
    
        "how many people would be in your party" : ("how many are you",
            "how many are you",
            "how many people would be in your party",
            "how many people would be in your party",
            "may i know how many guests will be at your table",
            "would you mind telling me how many guests shall be at your table"),
        
        "api_call" : ("api_call",
            "api_call",
            "api_call",
            "api_call",
            "api_call",
            "api_call"),
        
        "sure is there anything else to update" : ("cool anything else you want to update",
            "awesome is there any other update",
            "great is there anything else to modify",
            "great is there any other thing to modify",
            "i will modify your request is there anything else to change",
            "i shall modify your reservation is there any other change"),
        
        "ok let me look into some options for you" : ("ok looking for options",
            "sure finding some options",
            "ok sir i'm looking for options for you",
            "sure maam i'm finding some options for you",
            "excellent sir please give me a moment to provide you with options",
            "thank you madam i shall provide you with options shortly"),
        
        "what do you think of this option:" : ("is this one cool:",
            "how about this one:",
            "is this a good option:",
            "what do you think of this option:",
            "may i suggest this option:",
            "would you consider this option:"),
        
        "sure let me find an other option for you" : ("ok looking for something else",
            "sure finding something else",
            "ok i'll look for a better option",
            "sure i'll find a better option",
            "yes sir i will look for another suitable option",
            "yes maam i shall find another suitable option"),
        
        "here it is" : ("here you go",
            "here you go",
            "here it is",
            "here it is",
            "here is the infomation you asked for",
            "here is the infomation you asked for"),
        
        "is there anything i can help you with" : ("want anything else",
            "need something else",
            "is there anything i can help you with",
            "can i assist you with something else",
            "may i help you in any other way sir",
            "could i assist you in some other manner madam"),
        
        "great let me do the reservation" : ("cool its done",
            "awesome you are done",
            "great i'll finalise the request",
            "great let me do the reservation",
            "excellent i will finalise your request",
            "thank you i shall finish your reservation"),
        
        "you're welcome" : ("no problem",
            "happy to help",
            "you're welcome",
            "you're welcome",
            "it was a pleasure to be of help to you sir",
            "i am grateful to assist you madam")                
    }
    
    # Task 1
    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task1-API-calls-dev.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task1-API-calls-dev.txt', True)
    
    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task1-API-calls-trn.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task1-API-calls-trn.txt', True)
    
    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task1-API-calls-tst.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task1-API-calls-tst.txt', True)

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task1-API-calls-tst-OOV.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task1-API-calls-tst-OOV.txt', True)
    
    # Task 2
    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task2-API-refine-dev.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task2-API-refine-dev.txt', True)
    
    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task2-API-refine-trn.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task2-API-refine-trn.txt', True)
    
    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task2-API-refine-tst.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task2-API-refine-tst.txt', True)

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task2-API-refine-tst-OOV.txt')
    new_dialogs = modify_babi(dialogs, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task2-API-refine-tst-OOV.txt', True)
    
    # Candidates
    new_candidates = modify_candidates('dialog-bAbI-tasks/dialog-babi-candidates.txt', utterences)
    save_candidates(new_candidates, 'modified-tasks/modified-candidates.txt', True)