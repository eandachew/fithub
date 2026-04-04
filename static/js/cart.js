// Cart functionality for FitHub

document.addEventListener('DOMContentLoaded', function() {
    
    // Function to update cart via AJAX
    function updateCart(productId, newQuantity) {
        const url = `/shop/update/${productId}/`;
        
        // Show loading state
        const row = document.getElementById(`product-${productId}`);
        const quantityInput = row.querySelector('.quantity-input');
        const decrementBtn = row.querySelector('.decrement-btn');
        const incrementBtn = row.querySelector('.increment-btn');
        const removeBtn = row.querySelector('.remove-btn');
        const maxStock = parseInt(quantityInput.dataset.maxStock);
        
        // Check if new quantity exceeds stock
        if (newQuantity > maxStock) {
            showMessage(`Sorry, only ${maxStock} units available in stock!`, 'danger');
            return;
        }
        
        quantityInput.disabled = true;
        decrementBtn.disabled = true;
        incrementBtn.disabled = true;
        if (removeBtn) removeBtn.disabled = true;
        
        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: new URLSearchParams({
                'quantity': newQuantity
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {

                const productTotal = row.querySelector('.product-total');
                const cartTotal = document.getElementById('cart-total');
                
                quantityInput.value = data.quantity;
                
                productTotal.textContent = `€${data.total_price}`;
                
                cartTotal.textContent = `€${data.cart_total}`;
                
                if (data.quantity === 0) {
                    row.remove();
                
                    if (document.querySelectorAll('tbody tr').length === 0) {
                        location.reload();
                    }
                } else {
                    // Show success feedback
                    showTemporaryFeedback(row, 'success');
                }
            } else {
                showMessage(data.message || 'Error updating cart', 'danger');
                showTemporaryFeedback(row, 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showMessage('Error updating cart', 'danger');
            showTemporaryFeedback(row, 'error');
        })
        .finally(() => {
            // Re-enable inputs
            quantityInput.disabled = false;
            decrementBtn.disabled = false;
            incrementBtn.disabled = false;
            if (removeBtn) removeBtn.disabled = false;
        });
    }
    
    // Handle increment button click
    document.querySelectorAll('.increment-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            const row = document.getElementById(`product-${productId}`);
            const quantityInput = row.querySelector('.quantity-input');
            const maxStock = parseInt(quantityInput.dataset.maxStock);
            let currentQuantity = parseInt(quantityInput.value);
            const newQuantity = currentQuantity + 1;
            if (newQuantity <= maxStock) {
                updateCart(productId, newQuantity);
            } else {
                showMessage(`Maximum quantity is ${maxStock} (only ${maxStock} in stock)`, 'warning');
            }
        });
    });
    
    // Handle decrement button click
    document.querySelectorAll('.decrement-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            const row = document.getElementById(`product-${productId}`);
            const quantityInput = row.querySelector('.quantity-input');
            let currentQuantity = parseInt(quantityInput.value);
            const newQuantity = currentQuantity - 1;
            if (newQuantity >= 0) {
                updateCart(productId, newQuantity);
            }
        });
    });
    
    // Handle remove button click
    document.querySelectorAll('.remove-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            if (confirm('Are you sure you want to remove this item from your cart?')) {
                const productId = this.dataset.productId;
                updateCart(productId, 0);
            }
        });
    });
    
    // Helper function to show temporary visual feedback
    function showTemporaryFeedback(row, type) {
        const originalBg = row.style.backgroundColor;
        row.style.backgroundColor = type === 'success' ? '#d4edda' : '#f8d7da';
        setTimeout(() => {
            row.style.backgroundColor = originalBg;
        }, 500);
    }
});

// Helper function to show messages
function showMessage(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}