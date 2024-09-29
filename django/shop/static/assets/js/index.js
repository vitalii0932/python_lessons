let slideIndex = 0;
const slides = document.querySelectorAll('.slide');
const slideInterval = 3000;
let intervalId;

function nextSlide() {
	slideIndex = (slideIndex + 1) % slides.length;
	showSlides();
}

function showSlides() {
	const offset = -slideIndex * 100;
	slides.forEach(slide => {
		slide.style.transform = `translateX(${offset}%)`;
	});
}

function startSlider() {
	showSlides();
	intervalId = setInterval(nextSlide, slideInterval);
}

function stopSlider() {
	clearInterval(intervalId);
}

startSlider();

document.querySelector('.slider').addEventListener('mouseover', stopSlider);
document.querySelector('.slider').addEventListener('mouseout', startSlider);

function openModal() {
	document.getElementById('cartModal').style.display = 'block';
}

function closeModal() {
	document.getElementById('cartModal').style.display = 'none';
}

window.onclick = function (event) {
	if (event.target === document.getElementById('cartModal')) {
		closeModal();
	}
};

document.addEventListener("DOMContentLoaded", function() {
	const buttons = document.querySelectorAll(".buy_btn");
	
	buttons.forEach(button => {
		button.addEventListener("click", function(event) {
			const drugId = this.dataset.drugId;
			
			// Send AJAX request to add item to cart
			fetch(`/add-to-cart/${drugId}/`, {
				method: 'GET',
				headers: {
					'X-Requested-With': 'XMLHttpRequest',
				},
			})
			.then(response => response.json())
			.then(data => {
				alert(data.message); // Notify the user
			})
			.catch(error => {
				console.error("Error adding to cart:", error);
			});
		});
	});
});
