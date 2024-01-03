import React, { useState, useEffect } from 'react';

const Typewriter = ({ text, delay, infinite, onAnimationComplete }) => {
  const initialText = ' '.repeat(text.length);
  const [currentText, setCurrentText] = useState(initialText);
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    let timeout;

    if (currentIndex < text.length) {
      timeout = setTimeout(() => {
        setCurrentText((prevText) =>
          prevText.substring(0, currentIndex) + text[currentIndex] + prevText.substring(currentIndex + 1)
        );
        setCurrentIndex((prevIndex) => prevIndex + 1);
      }, delay);
    } else if (infinite) {
      setCurrentIndex(0);
      setCurrentText(initialText);
    } else if (onAnimationComplete) {
      onAnimationComplete();
    }

    return () => clearTimeout(timeout);
  }, [currentIndex, delay, infinite, text, onAnimationComplete, initialText]);

  return <span>{currentText}</span>;
};

export default Typewriter;
