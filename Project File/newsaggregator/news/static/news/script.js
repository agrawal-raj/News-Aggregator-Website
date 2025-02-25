const translateText = async (text, targetLang) => {
    try {
        const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|${targetLang}`;
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data.responseData.translatedText;
    } catch (error) {
        console.error('Translation error:', error);
        return text;  // Return the original text if translation fails
    }
};

const translatePage = async (targetLang) => {
    const spinner = document.getElementById('loading-spinner');
    spinner.style.display = 'block';  // Show spinner

    const elements = document.querySelectorAll('[data-translate]');
    for (const element of elements) {
        const text = element.innerText;
        const translatedText = await translateText(text, targetLang);
        element.innerText = translatedText;
    }

    spinner.style.display = 'none';  // Hide spinner
};

document.getElementById('translate-dropdown').addEventListener('change', (event) => {
    const targetLang = event.target.value;
    translatePage(targetLang);
});