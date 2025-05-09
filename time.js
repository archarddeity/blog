// time.js - Enhanced dynamic background with smarter time handling
const timeQualities = {
    dawn: { 
        range: [4, 6], 
        bg: 'linear-gradient(to bottom, #1a2a6c, #b21f1f, #fdbb2d)',
        blendMode: 'soft-light' // Warmer dawn effect
    },
    morning: { 
        range: [5, 11], 
        bg: 'linear-gradient(to bottom, #00c6fb 0%, #005bea 100%)',
        blendMode: 'overlay' // Crisp morning blues
    },
    midday: { 
        range: [12, 14], 
        bg: 'radial-gradient(circle, #56ccf2 0%, #2f80ed 100%)',
        blendMode: 'hard-light' // Vibrant overhead sun
    },
    afternoon: { 
        range: [15, 17], 
        bg: 'linear-gradient(to bottom, #f46b45, #eea849)',
        blendMode: 'multiply' // Golden warmth
    },
    sunset: { 
        range: [19, 21], 
        bg: 'linear-gradient(to bottom, #f12711, #f5af19 70%)',
        blendMode: 'color-dodge' // Glowing sunset
    },
    twilight: { 
        range: [18, 20], 
        bg: 'linear-gradient(to bottom, #0f2027, #203a43, #2c5364)',
        blendMode: 'darken' // Deepening shadows
    },
    evening: { 
        range: [18, 22], 
        bg: 'linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)',
        blendMode: 'exclusion' // Moody contrast
    },
    late_night: { 
        range: [22, 23], 
        bg: 'linear-gradient(to bottom, #000428, #004e92)',
        blendMode: 'luminosity' // Subtle depth
    },
    midnight: { 
        range: [0, 3], 
        bg: 'linear-gradient(to bottom, #000000, #434343)',
        blendMode: 'difference' // Stark darkness
    },
    night: { 
        range: [23, 4], 
        bg: 'radial-gradient(circle at center, #0a0a0a 0%, #1a1a1a 100%)',
        blendMode: 'normal' // Base night mode
    }
};

// Improved time quality detection (prioritizes specific ranges first)
function getCurrentTimeQuality() {
    const now = new Date();
    const currentHour = now.getHours();
    const currentMinute = now.getMinutes();
    
    // Special cases (e.g., sunset takes precedence over twilight if overlapping)
    if (currentHour >= 19 && currentHour <= 21 && currentMinute >= 30) return 'sunset';
    if (currentHour === 4 || (currentHour === 5 && currentMinute <= 30)) return 'dawn';
    
    // Check all other ranges
    for (const [quality, data] of Object.entries(timeQualities)) {
        const [start, end] = data.range;
        if (
            (start <= end && currentHour >= start && currentHour <= end) ||
            (start > end && (currentHour >= start || currentHour <= end))
        ) {
            return quality;
        }
    }
    return 'midday'; // Fallback
}

// Smoother background updates with transitions
function updateBackground() {
    const quality = getCurrentTimeQuality();
    const { bg, blendMode } = timeQualities[quality];
    
    document.body.style.transition = 'background-image 1.5s ease, background-blend-mode 1.5s ease';
    document.body.style.backgroundImage = `${bg}, url("https://picsum.photos/800/600?grayscale&rart=${Math.floor(Math.random() * 100)}")`;
    document.body.style.backgroundBlendMode = `${blendMode}, overlay`;
}

// Initialize with faster first load
updateBackground();

// Update every minute with random grayscale variation
setInterval(() => {
    updateBackground();
}, 60000);

// Optional: Update on visibility change (if user switches tabs)
document.addEventListener('visibilitychange', () => {
    if (!document.hidden) updateBackground();
});