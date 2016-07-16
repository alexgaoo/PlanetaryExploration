module DecPOMDP

export DecPOMDP

type DecPOMDP
    states::Matrix
    actions::Array
    observations::Matrix
    
    function DecPOMDP(states::Matrix, actions::Array, observations::Matrix)
        return new(states, actions, observations)
    end
end

end
    