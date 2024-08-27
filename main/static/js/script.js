function clearSearch(selected_input) {
    const input = document.querySelector('.' + selected_input);
    input.value = '';
    input.focus();
}
