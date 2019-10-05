% List interleaver for progressive rendering of 1D data | Lucas V. B.
% Returns an array from (start) to (end), inclusive.
% No restrictions at all on start or end values, other than being integers.
% Useful for "progressive rendering", by picking values at finer and finer resolutions last
% Example:
%     Interleaver1D(0,10)
% {0, 10, 5, 2, 7, 1, 3, 6, 8, 4, 9}
function order = Interleaver1D(from, to)
    if from > to
        tmp = to; to = from; from = tmp;
    end
    sec = [1, 1];
    order = [];
    secs = [];
    w = to - from;
    if w < 0
        return;
    end
    
    order = [from];
    if w == 0
        return;
    end
    order = [order, to];
    
    if w > 1
        secs = [[to-1,from+1],secs];
        while ~isempty(secs)
            sec(1) = secs(end); secs(end) = [];
            sec(2) = secs(end); secs(end) = [];
            w = sec(2) - sec(1);
            
            if w == 0
                order = [order,sec(1)];
                continue
            elseif w == 1
                order = [order,sec(1)];
                secs = [[sec(2),sec(2)], secs];
                continue
            end
            c = floor((sec(1) + sec(2)) / 2);
            order = [order, c];
            secs = [[sec(2),c+1,c-1,sec(1)], secs];
        end
    end
    
end