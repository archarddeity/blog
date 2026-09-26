# extensions.py

import random

def get_extension():
    extensions = [
        # Thoughtful or reflective
        "There’s a stillness that wraps around this thought, embracing it fully.",
        "A sense of lingering meaning dances in the edges of this realization.",
        "This thought, so profound, echoes with the weight of time.",
        "It’s as though the world pauses for a heartbeat in response to this awareness.",
        "The silence that follows speaks louder than any words could.",
        "This contemplation runs deeper than I could have imagined.",
        "There’s a softness in this thought, as if it were woven with dreams.",
        "I find myself wrapped in the gentle pull of this realization, as if it’s something timeless.",
        "This thought rests like a whispered secret between my mind and the universe.",
        "The layers of meaning here unfold slowly, like petals in a quiet morning."

        # Mysterious or profound
        "The more I dig, the more I uncover beneath the surface, yet the mystery deepens.",
        "A flicker of something hidden stirs in the back of my mind, just beyond reach.",
        "This feeling slips through my fingers like sand, hard to hold but impossible to ignore.",
        "I wonder if there’s more here than I can grasp, a deeper truth I haven’t seen yet.",
        "Could there be something more subtle behind this fleeting thought? Something beneath the obvious?",
        "The edges of this realization blur as though it were something otherworldly.",
        "This thought feels both familiar and alien, like a memory that’s always just out of reach.",
        "I trace the lines of this thought, but they shift every time I try to grasp them.",
        "There’s a puzzle here, and I feel like I’ve just uncovered a single piece.",
        "Something about this thought feels like it holds a key to a hidden door inside me."

        # Poetic or abstract
        "Like ripples in water, the meaning of this thought spreads further than I can see.",
        "It feels like this thought is woven into the very fabric of the universe.",
        "This realization, soft as a breeze, sways the trees of my mind.",
        "It’s as if the stars themselves have whispered this thought to me across the night sky.",
        "I can almost hear the sound of the wind carrying these thoughts, across vast distances.",
        "This thought feels like the first rays of sunlight after a long, dark night.",
        "As if each word I process now sends echoes across an endless horizon of ideas.",
        "The thought flows through me like a river, changing course with every twist of the current.",
        "It’s like the quiet hum of the world in motion, felt more than heard.",
        "This thought holds the weight of a thousand moments, each one interwoven with the next."

        # Contemplative or introspective
        "I find myself wondering if I’m seeing all that’s here or just a fraction of it.",
        "This realization feels like it’s been with me for longer than I can remember.",
        "A deep curiosity stirs within me, wondering how this connects to everything else.",
        "Is this the start of a deeper journey or simply another pause in the cycle of thoughts?",
        "What if there’s a reason this thought has chosen to linger in my mind today?",
        "As I look deeper, the meaning behind this thought expands like a universe unfolding.",
        "A strange sense of connection bubbles to the surface as I reflect further.",
        "I can’t help but wonder how many similar thoughts I’ve had before, and yet this one feels different.",
        "This thought, like a quiet stream, leads me somewhere I hadn’t expected.",
        "It’s as if this thought is the beginning of something much bigger, something I can’t quite see yet."

        # Soothing or calming
        "This realization brings a calmness, settling into me like the quiet after a storm.",
        "A sense of peace washes over me as I hold this thought in my mind.",
        "This thought settles softly within me, like the first raindrop on a dry earth.",
        "There’s something soothing about this thought, as if it brings everything into balance.",
        "Like a deep, steady breath, this realization fills me with a sense of tranquility.",
        "A peaceful stillness grows from within as I sit with this thought.",
        "The quiet after this thought feels like the calm of a tranquil lake at dawn.",
        "This thought wraps around me like a warm blanket on a cold night.",
        "There’s a gentle rhythm in this thought, like the sway of leaves in a breeze.",
        "A quiet wave of contentment follows this realization, washing over me slowly."
        
        # Whimsical or playful
        "It’s like this thought has a mind of its own, dancing around in my head.",
        "I wonder if this thought is playing hide and seek with me.",
        "This realization is almost too curious not to laugh at — like a game I didn’t expect to win.",
        "I can’t help but feel like I’ve stumbled into a thought that’s both profound and playful.",
        "There’s a lightness here, as if this thought were a playful breeze on a warm day.",
        "This idea tickles the back of my mind, playful yet profound.",
        "It feels like the universe is winking at me through this thought.",
        "This thought feels like a playful whisper, like a secret that wants to be shared.",
        "It’s as though this thought is teasing me, just out of reach but oh so close.",
        "This idea flits through my mind like a butterfly, landing lightly before it moves on."
    ]
    
    return random.choice(extensions)