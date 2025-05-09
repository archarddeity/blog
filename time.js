// time.js - Dynamic background based on local time

// Time qualities mapping
const timeQualities = {
    'dawn': { range: [4, 6], bg: 'linear-gradient(to bottom, #1a2a6c, #b21f1f, #fdbb2d)' },
    'morning': { range: [5, 11], bg: 'linear-gradient(to bottom, #00c6fb, #005bea)' },
    'midday': { range: [12, 14], bg: 'linear-gradient(to bottom, #56ccf2, #2f80ed)' },
    'afternoon': { range: [15, 17], bg: 'linear-gradient(to bottom, #f46b45, #eea849)' },
    'sunset': { range: [19, 21], bg: 'linear-gradient(to bottom, #f12711, #f5af19)' },
    'twilight': { range: [18, 20], bg: 'linear-gradient(to bottom, #0f2027, #203a43, #2c5364)' },
    'evening': { range: [18, 22], bg: 'linear-gradient(to bottom, #0f0c29, #302b63, #24243e)' },
    'late_night': { range: [22, 23], bg: 'linear-gradient(to bottom, #000428, #004e92)' },
    'midnight': { range: [0, 3], bg: 'linear-gradient(to bottom, #000000, #434343)' },
    'night': { range: [23, 4], bg: 'linear-gradient(to bottom, #0a0a0a, #1a1a1a)' }
};

function getCurrentTimeQuality() {
    const now = new Date();
    const currentHour = now.getHours();
    
    for (const [quality, data] of Object.entries(timeQualities)) {
        const [start, end] = data.range;
        
        if (start <= end) {
            if (currentHour >= start && currentHour <= end) {
                return quality;
            }
        } else {
            // Handle overnight ranges (like 23-4)
            if (currentHour >= start || currentHour <= end) {
                return quality;
            }
        }
    }
    
    return 'midday'; // default fallback
}

function updateBackground() {
    const quality = getCurrentTimeQuality();
    const bgStyle = timeQualities[quality].bg;
    
    document.body.style.backgroundImage = `${bgStyle}, url("https://picsum.photos/800/600?rart=3&grayscale")`;
    document.body.style.backgroundBlendMode = 'overlay, overlay';
}

// Initialize and update every minute
updateBackground();
setInterval(updateBackground, 60000);