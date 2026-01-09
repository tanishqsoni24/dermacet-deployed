// Professional Video Advertisement Handler
document.addEventListener('DOMContentLoaded', function() {
    const videoSection = document.querySelector('.video__advertisement--section');
    
    if (!videoSection) {
        console.log('Video section not found');
        return;
    }

    const video = videoSection.querySelector('.video__advertisement--video');
    const playPauseBtn = videoSection.querySelector('.video__play--pause');
    const muteBtn = videoSection.querySelector('.video__mute--toggle');
    const soundIndicator = videoSection.querySelector('.video__sound--indicator');
    const loadingSpinner = videoSection.querySelector('.video__loading');

    if (!video) {
        console.log('Video element not found');
        return;
    }

    console.log('Video element found, initializing...');

    // Try to play video immediately
    video.play().then(() => {
        console.log('Video playing successfully');
    }).catch(err => {
        console.log('Autoplay prevented:', err);
    });

    // Add error handling
    video.addEventListener('error', function(e) {
        console.error('Video error:', e);
        console.error('Video error code:', video.error ? video.error.code : 'unknown');
        console.error('Video error message:', video.error ? video.error.message : 'unknown');
    });

    video.addEventListener('loadstart', function() {
        console.log('Video loading started');
    });

    video.addEventListener('canplay', function() {
        console.log('Video can play');
    });

    // Auto-play video when it comes into view (muted)
    const observerOptions = {
        threshold: 0.5
    };

    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                video.play().catch(err => {
                    console.log('Autoplay prevented:', err);
                });
            } else {
                video.pause();
            }
        });
    }, observerOptions);

    videoObserver.observe(video);

    // Play/Pause functionality
    if (playPauseBtn) {
        playPauseBtn.addEventListener('click', function() {
            if (video.paused) {
                video.play();
                this.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z"/>
                    </svg>
                `;
                this.setAttribute('aria-label', 'Pause video');
            } else {
                video.pause();
                this.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M8 5v14l11-7z"/>
                    </svg>
                `;
                this.setAttribute('aria-label', 'Play video');
            }
        });
    }

    // Mute/Unmute functionality
    if (muteBtn) {
        muteBtn.addEventListener('click', function() {
            video.muted = !video.muted;
            
            if (video.muted) {
                this.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
                    </svg>
                `;
                this.setAttribute('aria-label', 'Unmute video');
                if (soundIndicator) {
                    soundIndicator.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
                        </svg>
                        <span>Muted</span>
                    `;
                }
            } else {
                this.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
                    </svg>
                `;
                this.setAttribute('aria-label', 'Mute video');
                if (soundIndicator) {
                    soundIndicator.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
                        </svg>
                        <span>Sound On</span>
                    `;
                }
            }
        });
    }

    // Hide loading spinner when video is ready
    video.addEventListener('loadeddata', function() {
        if (loadingSpinner) {
            loadingSpinner.style.display = 'none';
        }
    });

    // Update play button when video ends
    video.addEventListener('ended', function() {
        if (playPauseBtn) {
            playPauseBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z"/>
                </svg>
            `;
        }
    });

    // Click on video to play/pause
    video.addEventListener('click', function() {
        if (playPauseBtn) {
            playPauseBtn.click();
        }
    });
});
