module UAV

export UAV

type UAV
    state:: Vector{Float64}
    nStates:: Int64
    speed:: Float64

    function UAV(speed::Float64 
                 nStates::Int64 
        return new(zeros(nStates), nStates, speed)
    end 
end



end