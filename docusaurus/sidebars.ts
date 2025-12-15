import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Manual sidebar for our Physical AI textbook
  tutorialSidebar: [
    {
      type: 'category',
      label: 'AI-Native Physical AI & Humanoid Robotics Textbook',
      items: [
        {
          type: 'category',
          label: 'Part I: Foundations',
          items: [
            'chapter-1-introduction-to-physical-ai/index',
            'chapter-2-basics-of-humanoid-robotics/index'
          ],
        },
        {
          type: 'category',
          label: 'Part II: Technologies',
          items: [
            'chapter-3-ros-2-fundamentals/index',
            'chapter-4-digital-twin-simulation/index',
            'chapter-5-vision-language-action-systems/index'
          ],
        },
        {
          type: 'category',
          label: 'Part III: Integration',
          items: [
            'chapter-6-capstone/index'
          ],
        }
      ],
    }
  ],
};

export default sidebars;
