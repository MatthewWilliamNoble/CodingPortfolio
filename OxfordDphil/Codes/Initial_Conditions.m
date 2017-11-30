%%%% Bubble Lattice

function [t, A, B] = Initial_Conditions(n, base_SIA, base_vac, sig_SIA, sig_vac)

t = 0;

A = base_vac .* ones(n);

for i = 1 : 10 : n
    for j = 1 : 10 : n
        if rand >= 0.5
            A(i, j) = A(i,j) + sig_vac*rand;
        elseif rand < 0.5
            A(i, j) = A(i,j) - sig_vac*rand;
        end
    end
end

B = base_SIA .* ones(n);

end



% %%%% Cahn Hilliard Cook
%
% function [t, A, B] = initial_conditions(n, base, sig)
%
% t = 0;
%
% A = base.*ones(n);
%
% % A(51:60 ,51:70) = 1;
% % A(61:80,71:80) = 1;
%
% for i = 1 : n
%     for j = 1:n
%         if rand >= 0.5
%             A(i, j) = A(i,j) + sig*rand;
%         elseif rand <0.5
%             A(i, j) = A(i,j) - sig*rand;
%         end
%     end
% end
%
% B = base.* ones(n);
% end



% % %%%% Cahn Hilliard
% %
% % function [t, A, B] = initial_conditions(n, base, sig)
% %
% % t = 0;
% %
% % A = base.*ones(n);
% %
% % % A(51:60 ,51:70) = 1;
% % % A(61:80,71:80) = 1;
% %
% % for i = 1 : n
% %     for j = 1:n
% %         if rand >= 0.5
% %             A(i, j) = A(i,j) + sig*rand;
% %         elseif rand <0.5
% %             A(i, j) = A(i,j) - sig*rand;
% %         end
% %     end
% % end
% %
% % B = ones(n);
% % end

% %%%%    Gray-Scott
% 
% function [t, A, B] = Initial_Conditions(n)
% 
% t = 0;
% 
% A = ones(n);
% 
% B = zeros(n);
% 
% B(51:60 ,51:70) = 1;
% B(61:80,71:80) = 1;
% 
% % for i = 1 : 25 : n
% %     for j = 1 : 25 : n
% %         if rand >= 0.5
% %             B(i, j) = B(i,j) + rand;
% %         elseif rand < 0.5
% %             B(i, j) = B(i,j) - rand;
% %         end
% %     end
% % end
% 
% end