# subjects.py

def get_subjects(current_period):
    subjects = {
        'morning': [
            'dawn light', 'new possibilities', 'sleepy consciousness', 'early haze',
            'first light', 'growing warmth', 'faint birdsong', 'morning mist', 'sunrise',
            'fresh breath of day', 'awakening world', 'silent moments before time moves',
            'dew on grass', 'morning fog', 'half-formed thoughts', 'fragrance of coffee',
            'soft morning breeze', 'light through windows', 'stretching limbs', 'new beginnings',
            'endless potential', 'crisp air', 'reawakening', 'hopeful silence'
        ],
        'afternoon': [
            'passing hours', 'shifting shadows', 'daily rhythms', 'endless sun', 'bright sky',
            'lazy hours', 'noon heat', 'whispers of life', 'bustling crowds', 'hidden pauses',
            'drifting thoughts', 'the weight of time', 'distant conversations', 'bright afternoons',
            'fading light', 'subtle movements', 'overhead sun', 'the hum of the world',
            'softly closing doors', 'fleeting moments', 'crashing waves', 'flickering lights',
            'increasing tension', 'the drone of time', 'summertime buzz', 'afternoon silence'
        ],
        'evening': [
            'fading light', 'accumulated moments', 'day\'s impressions', 'setting sun', 'dying daylight',
            'long shadows', 'quietude', 'evening stillness', 'sunset glow', 'fading warmth',
            'end of a chapter', 'twilight whispers', 'lingering dusk', 'silent fading',
            'evening breeze', 'the approach of night', 'longing for peace', 'soft golden hues',
            'golden hour', 'slowly closing day', 'final moments of light', 'dimming horizon',
            'night’s quiet promise', 'day’s last breath', 'gathering peace', 'hopeful release'
        ],
        'night': [
            'starry silence', 'lonely hours', 'nocturnal musings', 'dark whispers', 'silent moonlight',
            'night air', 'hidden thoughts', 'deep stillness', 'insomniac thoughts', 'whispering shadows',
            'twinkling stars', 'silver light', 'midnight echoes', 'the quiet of solitude',
            'dreams waiting to form', 'heavy eyelids', 'unspoken secrets', 'full moon’s glow',
            'forgotten memories', 'distant lights', 'lonely streets', 'night’s embrace', 'night birds',
            'unseen world', 'serenity of darkness', 'nocturnal reflections'
        ],
        'dawn': [
            'first light', 'shimmering horizon', 'awakening earth', 'sleepy eyes', 'soft golden glow',
            'silent horizon', 'peaceful arrival', 'tender whispers of morning', 'cool air',
            'the quiet before movement', 'gradual awakening', 'peaceful world', 'the first breath',
            'light creeping in', 'soft morning fog', 'first stirrings of life', 'dreams fading',
            'early stillness', 'hidden sun', 'the first steps', 'shifting shadows', 'time slowing',
            'calm before rush', 'hope in the air', 'faint sounds of day approaching'
        ],
        'dusk': [
            'long shadows', 'fading colors', 'cool evening air', 'closing thoughts', 'the silence of dusk',
            'dimmed light', 'slowing pace', 'lingering warmth', 'hazy outlines', 'moonrise',
            'fading laughter', 'last moments of day', 'silence grows', 'the edge of night',
            'quiet sky', 'distant stars', 'sinking sun', 'flickering lights', 'calm nightfall',
            'whispers of dusk', 'the pull of rest', 'solitary hums', 'night closing in', 'silent earth',
            'final rays of light', 'gentle twilight'
        ],
        'twilight': [
            'the edge of night', 'dimming skies', 'final thoughts of the day', 'twilight haze', 'glowing edges',
            'indigo skies', 'fading horizon', 'twinkling stars just appearing', 'soft evening calls',
            'the quiet before night', 'peaceful shadows', 'fading glow', 'the balance of day and night',
            'distant murmurs', 'the glow of distant streetlights', 'slow quiet time', 'deepening blue',
            'restful peace', 'subtle stillness', 'the world slowing down', 'the golden afterglow',
            'shifting light', 'final glimpses of sun', 'whispers of stars'
        ],
        'midnight': [
            'moon’s peak', 'the heart of night', 'deep shadows', 'cold quiet', 'silver whispers',
            'midnight silence', 'dreamless hours', 'solitary thoughts', 'the void', 'frozen time',
            'midnight hums', 'the unseen hours', 'midnight breaths', 'hazy vision', 'deep dark sky',
            'uncertain thoughts', 'silence is loud', 'endless midnight', 'frozen world', 'heavy thoughts',
            'pulse of the moon', 'serene isolation', 'the pause of sleep', 'the night’s mystery'
        ],
        'storm': [
            'thunderclaps', 'howling winds', 'fury of rain', 'dark clouds', 'restless air',
            'flash of lightning', 'raging tempest', 'whipping winds', 'clashing forces', 'pouring rain',
            'the storm’s roar', 'swirling chaos', 'pounding hail', 'darkened sky', 'flickering lights',
            'turbulent waves', 'stormy whispers', 'crashing thunder', 'the earth’s shaking', 'rain’s lullaby',
            'the storm’s song', 'unrelenting fury', 'howling silence', 'quiet after storm'
        ],
        'bliss': [
            'contented sighs', 'soft smiles', 'warm embraces', 'tender moments', 'still joy',
            'peaceful laughter', 'delightful stillness', 'serene warmth', 'gentle rays of light',
            'inner peace', 'quiet ecstasy', 'satisfaction in silence', 'floating bliss', 'weightless joy',
            'harmonious hums', 'sweet serenity', 'soft whispers of happiness', 'tender happiness',
            'the warmth of love', 'unspoken understanding', 'soft joy', 'everlasting bliss', 'peaceful heart'
        ],
        'chaotic': [
            'rushing thoughts', 'spinning world', 'frenzied minds', 'uncontrolled actions', 'clashing voices',
            'shattered pieces', 'tangled wires', 'unsteady steps', 'blurring moments', 'wild thoughts',
            'unhinged laughter', 'unsynchronized pulses', 'erratic rhythm', 'conflicting forces', 'rising tension',
            'storming hearts', 'unraveled time', 'shattered silence', 'rumbling noises', 'loud chaos',
            'rampant energy', 'scattered plans', 'disrupted balance', 'unstable forces', 'intense confusion'
        ]
    }

    # Default fallback — night
    return subjects.get(current_period, subjects['night'])
