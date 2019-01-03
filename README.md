# Interleaver

*Interleaver* is a utility algorithm for progressive rendering of 1D and 2D data for faster visual results and evaluation. Instead of rendering data sequentially in your code, you can use *Interleaver* to get a list of data points to render: first for the edges, then the center point, then the points between those and so forth, always "filling in" the gaps. In 2D, it performs a recursive binary masking, overlaid on top of the image.

This effectively gives you a one-by-one rendering order for coarse-to-fine rendering of your datra.

I originally developed this for smarter rendering of my [Wikipedia animations](https://en.wikipedia.org/wiki/User:LucasVB/Gallery). I would be able to see the first frame, the last frame, then the middle frame, and as the rendering progressed I could quickly get a glimpse of the whole thing before the full animation was rendered. This allowed me to spot mistakes and errors earlier on and abort the rendering process.

This was inspired by traditional animation, in which [key frames](https://en.wikipedia.org/wiki/Key_frame) are drawn first to get a rough idea of the animation. The animator then goes back drawing (or [inbetweening](https://en.wikipedia.org/wiki/Inbetweening)) the remaining frames.

Eventually, I realized this function can be really useful in all sorts of other scenarios, like computer simulations that can be rendered in parallel. We can see the results of our work *much* faster by using this function.

Below are simple examples of how faster you can undertand pictures by virtue of *Interleaver*'s data order.

![Interleaver for 1D data](https://raw.githubusercontent.com/1ucasvb/interleaver/master/example_1d.gif)

In 1D, we can understand this function's shape with about a quarter of the final data.

![Interleaver for 2D data](https://raw.githubusercontent.com/1ucasvb/interleaver/master/example_2d.gif)

There are no size restrictions for either the 1D or 2D functions.

(The algorithms could probably be greatly simplified with some clever math magic, but I haven't looked into it much. I've just been using the old function that has done the trick all these years.)
