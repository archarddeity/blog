// time.js - Hyper-Precise Hourly Backgrounds
const hourlyThemes = {
    0: { // Midnight (12AM-1AM)
        bg: 'linear-gradient(to bottom, #000000, #1a1a2e)',
        blendMode: 'difference',
        label: '🌌 Deep Night'
    },
    1: { // 1AM-2AM
        bg: 'linear-gradient(to bottom, #0f0c29, #1d2671)',
        blendMode: 'exclusion',
        label: '🌠 Starlight'
    },
    2: { // 2AM-3AM
        bg: 'linear-gradient(to bottom, #000428, #203a43)',
        blendMode: 'luminosity',
        label: '🌃 Late Night'
    },
    3: { // 3AM-4AM
        bg: 'linear-gradient(to bottom, #0a0a0a, #2c3e50)',
        blendMode: 'multiply',
        label: '🌑 Pre-Dawn'
    },
    4: { // 4AM-5AM (First Light)
        bg: 'linear-gradient(to bottom, #1a2a6c, #b21f1f)',
        blendMode: 'soft-light',
        label: '🌅 First Light'
    },
    5: { // 5AM-6AM (Dawn)
        bg: 'linear-gradient(to bottom, #b21f1f, #fdbb2d)',
        blendMode: 'hard-light',
        label: '🌄 Dawn'
    },
    6: { // 6AM-7AM (Sunrise)
        bg: 'linear-gradient(to bottom, #fdbb2d, #00c6fb)',
        blendMode: 'overlay',
        label: '🌤 Sunrise'
    },
    7: { // 7AM-8AM
        bg: 'linear-gradient(to bottom, #00c6fb, #005bea)',
        blendMode: 'screen',
        label: '☀️ Morning Light'
    },
    8: { // 8AM-9AM
        bg: 'linear-gradient(135deg, #005bea, #00d2ff)',
        blendMode: 'lighten',
        label: '🔵 Fresh Morning'
    },
    9: { // 9AM-10AM
        bg: 'radial-gradient(circle at top, #56ccf2, #2f80ed)',
        blendMode: 'color-dodge',
        label: '💎 Crystal Hours'
    },
    10: { // 10AM-11AM
        bg: 'linear-gradient(to right, #2f80ed, #56ccf2)',
        blendMode: 'soft-light',
        label: '🌊 Late Morning'
    },
    11: { // 11AM-12PM
        bg: 'conic-gradient(from 90deg, #56ccf2, #2f80ed, #56ccf2)',
        blendMode: 'hard-light',
        label: '⏳ High Noon'
    },
    12: { // 12PM-1PM
        bg: 'radial-gradient(circle, #2f80ed, #56ccf2)',
        blendMode: 'overlay',
        label: '🔆 Solar Peak'
    },
    13: { // 1PM-2PM
        bg: 'linear-gradient(to bottom, #56ccf2, #2f80ed)',
        blendMode: 'screen',
        label: '🏙 Afternoon Start'
    },
    14: { // 2PM-3PM
        bg: 'linear-gradient(to bottom, #f46b45, #eea849)',
        blendMode: 'multiply',
        label: '🟠 Golden Hours'
    },
    15: { // 3PM-4PM
        bg: 'linear-gradient(135deg, #eea849, #f46b45)',
        blendMode: 'color-burn',
        label: '🧡 Late Golden'
    },
    16: { // 4PM-5PM
        bg: 'linear-gradient(to bottom, #f12711, #f5af19)',
        blendMode: 'darken',
        label: '🔶 Pre-Sunset'
    },
    17: { // 5PM-6PM (Sunset)
        bg: 'linear-gradient(to bottom, #f5af19, #f12711)',
        blendMode: 'color-dodge',
        label: '🌇 Sunset'
    },
    18: { // 6PM-7PM
        bg: 'linear-gradient(to bottom, #f12711, #0f2027)',
        blendMode: 'exclusion',
        label: '🌆 Dusk'
    },
    19: { // 7PM-8PM
        bg: 'linear-gradient(to bottom, #0f2027, #203a43)',
        blendMode: 'luminosity',
        label: '🌃 Early Night'
    },
    20: { // 8PM-9PM
        bg: 'linear-gradient(135deg, #203a43, #2c5364)',
        blendMode: 'soft-light',
        label: '🌉 City Lights'
    },
    21: { // 9PM-10PM
        bg: 'linear-gradient(to bottom, #2c5364, #0f0c29)',
        blendMode: 'hard-light',
        label: '🌠 Evening Glow'
    },
    22: { // 10PM-11PM
        bg: 'linear-gradient(to bottom, #0f0c29, #000428)',
        blendMode: 'difference',
        label: '🌌 Late Evening'
    },
    23: { // 11PM-12AM
        bg: 'linear-gradient(to bottom, #000428, #000000)',
        blendMode: 'exclusion',
        label: '🌑 Midnight Approach'
    }
};

function updateBackground() {
    const now = new Date();
    const currentHour = now.getHours();
    const currentTheme = hourlyThemes[currentHour];
    
    // Debug info
    console.log(`🕒 Local Time: ${now.toLocaleTimeString()}`);
    console.log(`🎨 Theme: ${currentTheme.label}`);
    
    // Apply theme
    document.body.style.backgroundImage = `
        ${currentTheme.bg},
        url("https://picsum.photos/800/600?grayscale&rart=${Math.random()}")
    `;
    document.body.style.backgroundBlendMode = `${currentTheme.blendMode}, overlay`;
    
    // Smooth transition
    document.body.style.transition = `
        background-image 1.2s cubic-bezier(0.4, 0, 0.2, 1),
        background-blend-mode 1.2s ease
    `;
}

// Initialize with immediate update
updateBackground();

// Update every minute + on tab focus
setInterval(updateBackground, 60000);
document.addEventListener('visibilitychange', () => {
    if (!document.hidden) setTimeout(updateBackground, 300);
});