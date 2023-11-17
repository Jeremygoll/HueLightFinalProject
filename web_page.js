document.addEventListener('DOMContentLoaded', function () {
    const colorPicker = document.getElementById('colorPicker');
    const enterButton = document.getElementById('enterButton');
    const colorDisplay = document.getElementById('colorDisplay');

    function changeColor() {
        const selectedColor = colorPicker.value;
        colorDisplay.style.backgroundColor = selectedColor;
    }

    function handleEnterButtonClick() {
        changeColor();
    }

    // Add event listeners
    colorPicker.addEventListener('input', changeColor);
    enterButton.addEventListener('click', handleEnterButtonClick);
});
