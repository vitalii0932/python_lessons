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
