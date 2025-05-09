// Ultimate Hourly Theme Engine
const hourlyThemes = {
    0: { // Midnight
        bg: 'linear-gradient(to bottom, #000000, #1a1a2e)',
        text: '#e0e0ff',
        accent: '#a0a0ff',
        blendMode: 'difference',
        label: '🌌 Midnight'
    },
    1: {
        bg: 'linear-gradient(to bottom, #0f0c29, #1d2671)',
        text: '#d8d8ff',
        accent: '#9494ff',
        blendMode: 'exclusion',
        label: '🌠 Late Night'
    },
    2: {
        bg: 'linear-gradient(to bottom, #000428, #203a43)',
        text: '#c8e6ff',
        accent: '#82c4ff',
        blendMode: 'luminosity',
        label: '🌃 Night Owl'
    },
    3: {
        bg: 'linear-gradient(to bottom, #0a0a0a, #2c3e50)',
        text: '#e0f7fa',
        accent: '#80deea',
        blendMode: 'multiply',
        label: '🌑 Pre-Dawn'
    },
    4: { // First Light
        bg: 'linear-gradient(to bottom, #1a2a6c, #b21f1f)',
        text: '#ffecb3',
        accent: '#ffb74d',
        blendMode: 'soft-light',
        label: '🌅 First Light'
    },
    5: { // Dawn
        bg: 'linear-gradient(to bottom, #b21f1f, #fdbb2d)',
        text: '#fff3e0',
        accent: '#ffcc80',
        blendMode: 'hard-light',
        label: '🌄 Dawn'
    },
    6: { // Sunrise
        bg: 'linear-gradient(to bottom, #fdbb2d, #00c6fb)',
        text: '#1a237e',
        accent: '#534bae',
        blendMode: 'overlay',
        label: '🌤 Sunrise'
    },
    7: { // Morning
        bg: 'linear-gradient(to bottom, #00c6fb, #005bea)',
        text: '#0d47a1',
        accent: '#5472d3',
        blendMode: 'screen',
        label: '☀️ Morning'
    },
    12: { // Noon
        bg: 'radial-gradient(circle, #2f80ed, #56ccf2)',
        text: '#01579b',
        accent: '#4fc3f7',
        blendMode: 'overlay',
        label: '🔆 Noon'
    },
    17: { // Sunset
        bg: 'linear-gradient(to bottom, #f5af19, #f12711)',
        text: '#3e2723',
        accent: '#d84315',
        blendMode: 'color-dodge',
        label: '🌇 Sunset'
    },
    21: { // Evening
        bg: 'linear-gradient(to bottom, #2c5364, #0f0c29)',
        text: '#bbdefb',
        accent: '#64b5f6',
        blendMode: 'hard-light',
        label: '🌃 Evening'
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