// Ultimate Hourly Theme Engine
const hourlyThemes = {
    0: { // Midnight (12AM-1AM)
        bg: 'linear-gradient(to bottom, #000000, #1a1a2e)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'difference',
        label: '🌌 Deep Night'
    },
    1: { // 1AM-2AM
        bg: 'linear-gradient(to bottom, #0f0c29, #1d2671)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'exclusion',
        label: '🌠 Starlight'
    },
    2: { // 2AM-3AM
        bg: 'linear-gradient(to bottom, #000428, #203a43)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'luminosity',
        label: '🌃 Late Night'
    },
    3: { // 3AM-4AM
        bg: 'linear-gradient(to bottom, #0a0a0a, #2c3e50)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'multiply',
        label: '🌑 Pre-Dawn'
    },
    4: { // 4AM-5AM (First Light)
        bg: 'linear-gradient(to bottom, #1a2a6c, #b21f1f)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'soft-light',
        label: '🌅 First Light'
    },
    5: { // 5AM-6AM (Dawn)
        bg: 'linear-gradient(to bottom, #b21f1f, #fdbb2d)',
        accent: '#000',
        text: '#000',
        blendMode: 'hard-light',
        label: '🌄 Dawn'
    },
    6: { // 6AM-7AM (Sunrise)
        bg: 'linear-gradient(to bottom, #fdbb2d, #00c6fb)',
        accent: '#000',
        text: '#000',
        blendMode: 'overlay',
        label: '🌤 Sunrise'
    },
    7: { // 7AM-8AM
        bg: 'linear-gradient(to bottom, #00c6fb, #005bea)',
        accent: '#000',
        text: '#000',
        blendMode: 'screen',
        label: '☀️ Morning Light'
    },
    8: { // 8AM-9AM
        bg: 'linear-gradient(135deg, #005bea, #00d2ff)',
        accent: '#000',
        text: '#000',
        blendMode: 'lighten',
        label: '🔵 Fresh Morning'
    },
    9: { // 9AM-10AM
        bg: 'radial-gradient(circle at top, #56ccf2, #2f80ed)',
        accent: '#000',
        text: '#000',
        blendMode: 'color-dodge',
        label: '💎 Crystal Hours'
    },
    10: { // 10AM-11AM
        bg: 'linear-gradient(to right, #2f80ed, #56ccf2)',
        accent: '#000',
        text: '#000',
        blendMode: 'soft-light',
        label: '🌊 Late Morning'
    },
    11: { // 11AM-12PM
        bg: 'conic-gradient(from 90deg, #56ccf2, #2f80ed, #56ccf2)',
        accent: '#000',
        text: '#000',
        blendMode: 'hard-light',
        label: '⏳ High Noon'
    },
    12: { // 12PM-1PM
        bg: 'radial-gradient(circle, #2f80ed, #56ccf2)',
        accent: '#000',
        text: '#000',
        blendMode: 'overlay',
        label: '🔆 Solar Peak'
    },
    13: { // 1PM-2PM
        bg: 'linear-gradient(to bottom, #56ccf2, #2f80ed)',
        accent: '#000',
        text: '#000',
        blendMode: 'screen',
        label: '🏙 Afternoon Start'
    },
    14: { // 2PM-3PM
        bg: 'linear-gradient(to bottom, #f46b45, #eea849)',
        accent: '#000',
        text: '#000',
        blendMode: 'multiply',
        label: '🟠 Golden Hours'
    },
    15: { // 3PM-4PM
        bg: 'linear-gradient(135deg, #eea849, #f46b45)',
        accent: '#000',
        text: '#000',
        blendMode: 'color-burn',
        label: '🧡 Late Golden'
    },
    16: { // 4PM-5PM
        bg: 'linear-gradient(to bottom, #f12711, #f5af19)',
        accent: '#000',
        text: '#000',
        blendMode: 'darken',
        label: '🔶 Pre-Sunset'
    },
    17: { // 5PM-6PM (Sunset)
        bg: 'linear-gradient(to bottom, #f5af19, #f12711)',
        accent: '#000',
        text: '#000',
        blendMode: 'color-dodge',
        label: '🌇 Sunset'
    },
    18: { // 6PM-7PM
        bg: 'linear-gradient(to bottom, #f12711, #0f2027)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'exclusion',
        label: '🌆 Dusk'
    },
    19: { // 7PM-8PM
        bg: 'linear-gradient(to bottom, #0f2027, #203a43)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'luminosity',
        label: '🌃 Early Night'
    },
    20: { // 8PM-9PM
        bg: 'linear-gradient(135deg, #203a43, #2c5364)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'soft-light',
        label: '🌉 City Lights'
    },
    21: { // 9PM-10PM
        bg: 'linear-gradient(to bottom, #2c5364, #0f0c29)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'hard-light',
        label: '🌠 Evening Glow'
    },
    22: { // 10PM-11PM
        bg: 'linear-gradient(to bottom, #0f0c29, #000428)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'difference',
        label: '🌌 Late Evening'
    },
    23: { // 11PM-12AM
        bg: 'linear-gradient(to bottom, #000428, #000000)',
        accent: '#FFF',
        text: '#FFF',
        blendMode: 'exclusion',
        label: '🌑 Midnight Approach'
    }
};

// Convert hex to RGB
function hexToRgb(hex) {
    const r = parseInt(hex.slice(1, 3), 16),
          g = parseInt(hex.slice(3, 5), 16),
          b = parseInt(hex.slice(5, 7), 16);
    return `${r}, ${g}, ${b}`;
}

// Apply all theme styles
function applyTheme(theme) {
    const rgbText = hexToRgb(theme.text);
    
    // Background
    document.body.style.backgroundImage = `
        ${theme.bg},
        url("https://picsum.photos/800/600?grayscale&rart=${Math.random()}")
    `;
    document.body.style.backgroundBlendMode = `${theme.blendMode}, overlay`;
    
    // CSS Variables
    document.documentElement.style.setProperty('--text-color', theme.text);
    document.documentElement.style.setProperty('--accent-color', theme.accent);
    document.documentElement.style.setProperty('--text-rgb', rgbText);
    
    // Content Box
    const postContent = document.querySelector('.post-content');
    if (postContent) {
        postContent.style.backgroundColor = `rgba(${rgbText}, 0.08)`;
        postContent.style.boxShadow = `0 0 20px rgba(${hexToRgb(theme.accent)}, 0.15)`;
    }
    
    console.log(`🕒 Active Theme: ${theme.label}`);
}

// Initialize theme system
function initThemeEngine() {
    // Create CSS variables
    const style = document.createElement('style');
    style.textContent = `
        :root {
            --text-color: #333;
            --accent-color: #8b4513;
            --text-rgb: 51, 51, 51;
            transition: all 1.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
    `;
    document.head.appendChild(style);
    
    // Update every minute
    function updateTheme() {
        const hour = new Date().getHours();
        const theme = hourlyThemes[hour] || hourlyThemes[12]; // Default to noon
        applyTheme(theme);
    }
    
    updateTheme();
    setInterval(updateTheme, 60000);
    document.addEventListener('visibilitychange', () => {
        if (!document.hidden) setTimeout(updateTheme, 300);
    });
}

// Start the engine!
initThemeEngine();