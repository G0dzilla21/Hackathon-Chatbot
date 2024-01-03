import React, { useState, useEffect } from "react";
import "../style/Hero.css";
import Typewriter from "./Typewriter";

const Hero = () => {
  const [cardSentences, setCardSentences] = useState([
    " 100-character mention for my product.",
    " product description for my service.",
    " list of 5 YouTube video ideas for me",
    " weekly newsletter topic",
  ]);
  const timeToDisplayEachSentence = 3000;
  const [currentSentenceIndex, setCurrentSentenceIndex] = useState(0);

  useEffect(() => {
    const totalDuration = cardSentences.length * timeToDisplayEachSentence;
    const intervalId = setInterval(() => {
      setCurrentSentenceIndex(
        (prevIndex) => (prevIndex + 1) % cardSentences.length
      );
    }, totalDuration);

    return () => clearInterval(intervalId);
  }, [cardSentences.length]);

  const handleTypewriterComplete = () => {
    setCurrentSentenceIndex(
      (prevIndex) => (prevIndex + 1) % cardSentences.length
    );
  };

  return (
    <div className="hero-container">
      <div className="intro-card">
        <div className="intro-words">
          <h1>Welcome to Ferestha!</h1>
          <h2>Your loyal dev assistant!</h2>
        </div>
      </div>
      <div className="card-container">
        <div className="card-content">
          <p>
            Structure a
            <Typewriter
              text={cardSentences[currentSentenceIndex]}
              delay={100}
              infinite={true}
              onAnimationComplete={handleTypewriterComplete}
            />
          </p>
        </div>
      </div>
    </div>
  );
};

export default Hero;
