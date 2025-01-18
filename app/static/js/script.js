// External JavaScript for dynamic form submission

// Get references to the form and selection field
const form = document.getElementById('dynamicForm');
const selection = document.getElementById('selection');

// Add an event listener to handle form submission
form.addEventListener('submit', function(event) {
    // Prevent default submission behavior
    event.preventDefault();

    // Get the selected value from the dropdown
    const selectedValue = selection.value;

    // Define a mapping between dropdown values and corresponding routes
    const routes = {
        personal: '/personal',
        team: '/team',
        authority: '/authority',
        ap: '/ap',
        employee: '/employee'
    };

    // Dynamically set the form's action attribute based on the selected value
    form.action = routes[selectedValue] || '/default';

    // Log the selected route for debugging purposes
    console.log('Form action set to:', form.action);

    // Submit the form to the dynamically set action
    form.submit();
});